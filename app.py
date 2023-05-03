# Imports the OpenAI API and Streamlit libraries.
import openai
import streamlit as st
from streamlit_chat import message
import toml
from utils import *
from PIL import Image
import streamlit.components.v1 as components
# import pyperclip

# with open('secrets.toml', 'r') as f:
#     config = toml.load(f)

# openai.api_key = config['api_key']
openai.api_key = st.secrets.api_key
fav = Image.open("./images/favicon.ico")
# The 'openai.api_key' is set to the API key manually retrieved from the Azure OpenAI Service resource.
# openai.api_key = "PLEASE_ENTER_YOUR_OWN_API_KEY"
# The 'openai.api_key' is set to the API key retrieved from the Streamlit secrets manager.

# Streamlit to set the page header and icon.
st.set_page_config(
        page_title="AG-BOT",
        page_icon=fav)

st.markdown("""
       <style>
       [data-testid="stSidebar"][aria-expanded="true"]{
           min-width: 485px;
           max-width: 485px;
       }
       #MainMenu {visibility: hidden;}
       footer {visibility: hidden;}
       """, unsafe_allow_html=True)


with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

col1, col2 = st.columns([1,8])
with col1:
    st.image(fav, width=72)
with col2:
    st.write("<p style='font-size:45px;'><b>AG-BOT</b>", unsafe_allow_html=True)

st.write("")
st.write("<p style='font-size:16px;'>AG-BOT은 멀티모델 데이터베이스 <b>AgensGraph</b>와 PostgreSQL 기반의 관계형 DBMS <b>AgensSQL</b>의 사용을 돕는 GPT 기반 챗봇입니다. 그래프 데이터베이스(GDB)에 사용되는 <b>Cypher</b>와 관계형 데이터베이스(RDB)에 사용되는 <b>PostgreSQL</b>을 챗봇을 통해 간편히 생성해보세요.</br></br><b>사용법: </b>좌측의 사이드바(<b> 〉 </b>)에서 원하는 작업을 선택한 후, TIP을 참고하여 질문을 입력하세요.", unsafe_allow_html=True)
st.write("")
st.write("")

# Deine the 'role' key as 'system' for the AI model's messages.
if 'prompts' not in st.session_state:
    st.session_state['prompts'] = [{"role": "system", "content": "You are Cypher language graph database helper."}]
# The 'generated' list stores the AI model's responses to the user's messages.
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
# The 'past' list stores the user's previous messages.
if 'past' not in st.session_state:
    st.session_state['past'] = []

def generate_response(prompt):
    st.session_state['prompts'].append({"role": "user", "content":prompt})
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                 max_tokens=2000,
                                 messages=st.session_state['prompts']
                                 )
    message=completion.choices[0].message.content
    return message

# The 'new_topic_click' function is defined to reset the conversation history and introduce the AI assistant.
def new_topic_click():
    st.session_state['prompts'] = [{"role": "system", "content": "You are Cypher language graph database helper."}]
    st.session_state['past'] = []
    st.session_state['generated'] = []
    st.session_state['user'] = ""

# and append the response to the conversation history.
def chat_click():
    if st.session_state['user'] != '':
        user_chat_input = st.session_state['user']
        output = generate_response(user_chat_input)
        st.session_state['past'].append(user_chat_input)
        st.session_state['generated'].append(output)
        st.session_state['prompts'].append({"role": "assistant", "content": output})
        st.session_state['user'] = ""
        
# with st.container():
with st.sidebar:
    st.write("")
    st.write("")
    task = st.selectbox("**수행할 작업을 선택하세요:**", tasks_list)
    st.write("")
    task2explanation(task)    
    instruction = task2instruction(task)
    st.session_state['prompts'] = [{"role": "system", "content": instruction}]
    st.write("")
    st.write("")
    prompt = st.text_area("**질문을 입력하세요:**", key='user')
    # st.write("")
    # submit = st.button(label="결과 출력", on_click=chat_click)
    col1, col2 = st.columns([4, 1])
    with col1:
        submit = st.button(label="**결과 출력**", on_click=chat_click)
    with col2:
        new_topic_button = st.button("**지우개**", on_click=new_topic_click)

#     # st.write("")
#     copy = st.button(label="**결과 복사**")
#     if copy:
#         if len(st.session_state['generated']) != 0:
#             pyperclip.copy(st.session_state['generated'][-1])
#             st.markdown("<p style='font-size:14px;'>복사되었습니다.</br>",unsafe_allow_html=True)
#         else:
#             st.markdown("<p style='font-size:14px;'>   결과를 먼저 출력해주세요.</br>",unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.markdown("<p style='font-size:12px;'>◦  API 서버의 상태에 따라 결과 출력이 지연될 수 있습니다.</br>◦  의도하지 않은 결과가 출력될 경우, 새로고침 후 다시 생성해보세요.", unsafe_allow_html=True)
    


if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['generated'][i], avatar_style='thumbs', key=str(i))
        message(st.session_state['past'][i], is_user=True, avatar_style='thumbs', key=str(i) + '_user')
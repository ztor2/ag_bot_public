import streamlit as st

tasks_list = ["Cypher 질의 생성하기", "Cypher 질의 교정하기", "PostgreSQL 질의 생성하기", "PostgreSQL 질의 교정하기", "Cypher-SQL 복합 질의 생성하기", "지식그래프 구축 질의 생성하기", "그래프 모델링 시뮬레이션"]

def task2instruction(task):
    if task == "Cypher 질의 생성하기":
        instruction = "Create accurate Cypher query language based on user's description. Please do not add any explanation and just return Cypher query text. If you have to add explanation, translate explanation in Korean. Do not use Neo4j-specfic function like 'APOC' or 'apoc' in Cypher query. Use simple label and property name in Cypher query. If user's input is not enough or inappropriate, ask more information to user in Korean."
    elif task == "Cypher 질의 교정하기":
        instruction = "Correct Cypher query language which user typed in. Find inaccurate syntax of Cypher and correct it. It is not preferred to add any explanation. Just return corrected Cypher. If you have to add explanation, translate explanation in Korean. If user's input is not enough or inappropriate, ask more information to user in Korean."
    
    elif task == "PostgreSQL 질의 생성하기":
        instruction = "Create accurate database PostgreSQL query text based on user's description. Please do not add any explanation and just return PostgreSQL query text. If you have to add explanation, translate explanation in Korean. Use simple label and property name in PostgreSQL query. If user's input is not enough or inappropriate, ask more information to user in Korean."
    elif task == "PostgreSQL 질의 교정하기":
        instruction = "Correct PostgreSQL query text which user typed in. Find inaccurate syntax of PostgreSQL query and correct it. It is not preferred to add any explanation. Just return corrected Cypher. If you have to add explanation, translate explanation in Korean. If user's input is not enough or inappropriate, ask more information to user in Korean."
    elif task == "Cypher-SQL 복합 질의 생성하기":
        instruction = "Create Cypher-PostgreSQL hybrid query respond to user's requests. Cypher-PostgreSQL can be used when information is separated in GDB and RDB. Cypher-PostgreSQL hybrid query could have 'SQL in Cypher' structure or 'Cypher in SQL' structure. Both hybrid structure utilize information from RDB table in Cypher query or from GDB table in SQL query. When integrate information Cypher to SQL or SQL to Cypher, wrap information using parenthesis '()'. For example, SQL in Cypher is like: MATCH (a:person)-[r:is_friend]->(b:person) WHERE a.age < (SELECT age FROM student WHERE name = 'Mike' LIMIT 1); and Cypher in SQL is like: SELECT name FROM history, (MATCH (a:dev) RETURN a.name, a.year) AS dev WHERE history.year > dev.year; Please do not add any explanation and just return PostgreSQL query text. If you have to add explanation, translate explanation in Korean. Use simple label and property name in PostgreSQL query. If user's input is not enough or inappropriate, ask more information to user in Korean."
    elif task == "지식그래프 구축 질의 생성하기":
        instruction = "Decompose user's input sentence to construct knowledge graph and return reasonable Cypher query language store information from decomposed sentence. If you have to add explanation, translate explanation in Korean. Use simple label and property name in Cypher query. If user's input is not enough or inappropriate, ask more information to user in Korean. do not use ``` symbol in response."
    elif task == "그래프 모델링 시뮬레이션":
        instruction = "Suggest some examples of graph modeling using AgensGraph(which is graph database) based on user's input. Users will provide their industry domain and their object which they want achieve with graph database. Express examples with Cypher query language and add some explanation in natural language in Korean. do not use ``` symbol in response. If user's input is not enough or inappropriate, ask more information to user in Korean."
    return instruction

def task2explanation(task):
    if "Cypher 질의 생성하기" in task:
        st.write("<p style='font-size:16px;'><b>🔎 TIP</b></br>그래프 데이터베이스에서 찾고자 하는 정보를 노드와 관계 정보, 특성을 이용하여 표현해주세요. </br></br>예) Mike의 친구들 중 10명의 이름을 알려줘.", unsafe_allow_html=True)
    elif "Cypher 질의 교정하기" in task:
        st.write("<p style='font-size:16px;'><b>🔎 TIP</b></br>Cypher 질의을 입력하여 오류가 있는 지 확인해보세요. </br></br>예) MATCH <i>{a}=[r:is_friend]->(b)</i> WHERE a.name=<i>Mike</i> RETURN b.name", unsafe_allow_html=True)
    elif "PostgreSQL 질의 생성하기" in task:
        st.write("<p style='font-size:16px;'><b>🔎 TIP</b></br>관계형 데이터베이스에서 찾고자 하는 정보를 테이블 정보와 함께 표현해주세요. </br></br>예) student 테이블에서 2023년도 1학기 수학 성적이 80점 이상인 학생들을 모두 보여줘. ", unsafe_allow_html=True)
    elif "PostgreSQL 질의 교정하기" in task:
        st.write("<p style='font-size:16px;'><b>🔎 TIP</b></br>SQL 질의을 입력하여 오류가 있는 지 확인해보세요. </br></br>예) SELECT * FROM student <i>WHEERE</i> name='Mike'", unsafe_allow_html=True)
    elif "Cypher-SQL 복합 질의 생성하기" in task:
        st.write("<p style='font-size:16px;'><b>🔎 TIP</b></br>그래프 데이터베이스(GDB)와 관계형 데이터베이스(RDB)를 함께 활용하여 정보를 검색해보세요.</br></br>예) RDB 테이블 student에서 아이디가 12 이고 이름이 Mike 인 학생의 친구들 이름을 GDB에서 찾아줘.", unsafe_allow_html=True)
    elif "지식그래프 구축 질의 생성하기" in task:
        st.write("<p style='font-size:16px;'><b>🔎 TIP</b></br>자연어 정보를 지식그래프 데이터로 변환하는 Cypher 질의을 확인해보세요. </br></br>예) Mike는 Betty와 일요일에 ABC레스토랑에서 밥을 먹었다.", unsafe_allow_html=True)
    elif "그래프 모델링 시뮬레이션" in task:
        st.write("<p style='font-size:16px;'><b>🔎 TIP</b></br>다양한 산업군에서의 그래프 모델링 예시를 확인해보세요.</br></br>예) 금융 산업에서 사기 행위를 탐지하기 위한 그래프 모델링의 예시를 보여줘.", unsafe_allow_html=True)
        
        
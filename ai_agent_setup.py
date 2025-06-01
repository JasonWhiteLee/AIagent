import streamlit as st
import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI

# Streamlit Cloud(share)에서는 secrets 관리 권장
# os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
os.environ["GOOGLE_API_KEY"] = (
    "YOUR_GOOGLE_API_KEY"  # 로컬 테스트용, 배포시 secrets 사용 권장
)

# 2. Google Generative AI 설정
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# 3. LangChain용 Google Generative AI 챗 모델 인스턴스 생성
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",  # 사용할 모델명 (예: gemini-pro, gemini-1.5-pro 등)
    temperature=0.7,  # 창의성(랜덤성) 조절
    max_output_tokens=1024,  # 출력 토큰 제한
)

st.title("Gemini AI 챗봇 데모")
st.write("Google Generative AI + LangChain 기반 간단 챗봇입니다.")

user_input = st.text_input("프롬프트를 입력하세요:")

if st.button("AI에게 물어보기"):
    if user_input:
        with st.spinner("AI가 답변을 생성 중입니다..."):
            response = llm.invoke(user_input)
        st.subheader("AI의 답변:")
        st.write(response)
    else:
        st.warning("프롬프트를 입력해주세요.")

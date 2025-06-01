import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. 환경 변수에 API 키 저장 (이미 저장되어 있다면 생략)
os.environ["GOOGLE_API_KEY"] = (
    "AIzaSyCS_t4PxR1GC_bF4ot9emDcdi8yqRMK9YM"  # 여기에 본인의 API 키를 입력하세요
)

# 2. Google Generative AI 설정
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# 3. LangChain용 Google Generative AI 챗 모델 인스턴스 생성
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",  # 사용할 모델명 (예: gemini-pro, gemini-1.5-pro 등)
    temperature=0.7,  # 창의성(랜덤성) 조절
    max_output_tokens=1024,  # 출력 토큰 제한
)

# 4. 간단한 프롬프트로 테스트
response = llm.invoke("안녕! 너는 어떤 일을 할 수 있어?")
print(response)

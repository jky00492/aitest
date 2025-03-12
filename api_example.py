from google import genai
import google.generativeai as genai

import speech_recognition as sr  # 음성 인식 라이브러리
import pyttsx3  # 텍스트를 음성으로 변환


# API 키 설정
# client = genai.Client(api_key="AIzaSyAjMMzhy3Wdaw-HNabHErP8u7pKp-3-pUQ")  # "YOUR_GEMINI_API_KEY"를 발급받은 키로 교체하세요.
genai.configure(api_key="AIzaSyAjMMzhy3Wdaw-HNabHErP8u7pKp-3-pUQ")


conversation_history = []
model = genai.GenerativeModel('gemini-2.0-flash')
chat = model.start_chat(history=[])

# 텍스트를 음성으로 재생 (선택적)
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# 음성 입력 처리
def listen_and_recognize():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("음성을 입력하세요...")
        try:
            # 음성 청취 후 텍스트 변환
            audio = recognizer.listen(source, timeout=5)
            user_input = recognizer.recognize_google(audio, language="ko-KR")  # 한국어 인식
            print(f"들린 내용: {user_input}")
            return user_input
        except sr.UnknownValueError:
            print("음성을 이해하지 못했습니다.")
            speak_text("죄송합니다. 이해하지 못했습니다.")
            return None
        except sr.RequestError as e:
            print(f"음성 인식 서비스 오류: {e}")
            speak_text("음성 인식 서비스에서 오류가 발생했습니다.")
            return None
                
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    response = chat.send_message(user_input, stream=True)

    # conversation_history.append({"content": user_input})

    # 텍스트 생성
    # response = client.models.generate_content(
    #     model="gemini-2.0-flash",
    #     # gemini-1.5-flash
    #     contents="api로 제미나이 호출했는데 사용량 확인은?",
    # )
    # response = client.models.generate_content(
    #     model="gemini-2.0-flash",
    #     # gemini-1.5-flash
    #     contents=conversation_history,  # 전체 대화 기록 전달
    #     # contents=user_input,  # 전체 대화 기록 전달
    # )

    # reply = response.text
    # print(f"Gemini: {reply}")
    for chunk in response:
        print(chunk.text, end='', flush=True)


    # 응답을 컨텍스트로 추가

    # conversation_history.append({"role": "assistant", "content": reply})
    # 결과 출력
    # print("생성된 텍스트:")
    # print(response.text)

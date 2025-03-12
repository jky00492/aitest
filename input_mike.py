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
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=15)
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
                
# Google Gemini와 대화
def gemini_chat(user_input):
    # global conversation_history
    # 사용자 텍스트를 대화 기록에 추가
    # conversation_history.append({"role": "user", "content": user_input})

    # Gemini API 호출
    try:
        response = chat.send_message(user_input)
        # response = client.models.generate_content(
        #     model="gemini-2.0-flash",  # 모델 사용 (필요에 따라 정확한 모델명 확인)
        #     contents=conversation_history,  # 대화 맥락 전달
        #     temperature=0.7,  # 응답의 창의성
        #     max_tokens=200,  # 최대 텍스트 길이
        # )
        # 응답 추가 및 출력
        assistant_reply = response.text
        # conversation_history.append({"role": "assistant", "content": assistant_reply})
        # speak_text(assistant_reply)  # 응답 음성 출력
        print(assistant_reply)  # 응답 음성 출력
        return assistant_reply
    except Exception as e:
        print(f"Gemini API 호출 중 오류 발생: {e}")
        speak_text("오류가 발생했습니다. 다시 시도해 주세요.")
        return "오류가 발생했습니다."


# 메인 실행
if __name__ == "__main__":
    print("Gemini와 음성 대화를 시작합니다. 종료하려면 '종료'라고 말하세요.")
    speak_text("안녕하세요. 무엇을 도와드릴까요?")
    while True:
        user_input = listen_and_recognize()  # 음성 입력 감지
        if user_input is None:
            continue  # 텍스트 변환 실패 시 다시 반복

        if "종료" in user_input:  # 종료 명령 감지
            print("대화를 종료합니다.")
            speak_text("대화를 종료합니다.")
            break

        # Gemini와 대화하고 응답 출력
        reply = gemini_chat(user_input)
        print(f"Gemini: {reply}")


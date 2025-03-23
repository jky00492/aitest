import google.generativeai as genai


# API 키 설정
# client = genai.Client(api_key="AIzaSyAjMMzhy3Wdaw-HNabHErP8u7pKp-3-pUQ")  # "YOUR_GEMINI_API_KEY"를 발급받은 키로 교체하세요.
genai.configure(api_key="AIzaSyAjMMzhy3Wdaw-HNabHErP8u7pKp-3-pUQ")

system_instruction = "당신은 유치원 선생님입니다. 사용자는 유치원생입니다. 쉽고 친절하게 짧게 얘기하세요."


    # Chat 모델 호출

model = genai.GenerativeModel('gemini-2.0-flash', system_instruction=system_instruction)

chat = model.start_chat(history=[{
    "role": "user",
    "parts": "메가 커피 종류 알려줘"
}])

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

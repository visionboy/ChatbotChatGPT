import openai

openai.api_key = "yuor api ke"

message = []
while True:
    user_content = input("user : ")
    message.append({"role": "user", "content": f"{user_content}"})

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=message)

    assistent_content = completion.choices[0].message["content"].strip()

    message.append({"role": "assistant", "content": f"{assistent_content}"})

    print(f"GPT: {assistent_content}")


import openai


openai.api_key="sk-rgugtbPBXEmfuTb5T1MNT3B1bkFJUsmgxLR5W4oy2S8JeYXt"
messages=[{"role":"system","content":"about chatgpt"}]

while True:
    messages=input("user:")
    if message:
        messages.append({"role":"user","content":message})
        chat=openai.chatcompletion.create(model="gpt-3.5-turbo",messages=messages,temperature=0.5)
        reply=chat.choices[0].message.content
        print(f"chatgpt:{reply}")
        messages.append({"role":"user","content":reply})


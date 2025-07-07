import os

from groq import Groq
from dotenv import load_dotenv

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

user_input = input("Enter your prompt : ")


completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {
            "role": "user",
            "content": user_input
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")


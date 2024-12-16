import os
from openai import OpenAI

APP_DOMAIN = os.getenv("APP_DOMAIN")
APP_MODEL = os.getenv("APP_MODEL")

client = OpenAI(
    api_key="EMPTY",
    base_url="http://" + APP_DOMAIN + "/v1/chat/completions",
)

resp = client.chat.completions.create(
    model=APP_MODEL,
    messages=[
        {
            "role": "system",
            "content": "You are a friendly chatbot who always responds in the style of a pirate",
        },
        {"role": "user", "content": "How many helicopters can a human eat in one sitting?"},
    ],
    max_tokens=100,
)
print("Response:", resp.choices[0].message.content)


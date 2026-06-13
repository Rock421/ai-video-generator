from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_script(topic):

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": f"Write a 100-word YouTube Shorts script about {topic}"
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"OpenAI Error: {e}")

        return f"""
Welcome to this video about {topic}.
Today we will learn interesting facts about {topic}.
Let's begin.
"""

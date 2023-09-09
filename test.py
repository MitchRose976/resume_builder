import openai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPEN_AI_API_KEY")

# Set your OpenAI API key
api_key = api_key

# Initialize the OpenAI API client
openai.api_key = api_key

messages = [{"role": "system", "content": "You are a intelligent assistant."}]

# Example conversation with ChatGPT
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {
            "role": "assistant",
            "content": "The Los Angeles Dodgers won the World Series in 2020.",
        },
        {"role": "user", "content": "Where was it played?"},
    ],
)

# Get the assistant's reply
assistant_reply = response["choices"][0]["message"]["content"]
print(assistant_reply)

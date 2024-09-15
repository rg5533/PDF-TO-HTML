import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Create the OpenAI client
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)
try:
    # Try to make a simple API call
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Hello, how are you?"}
        ]
    )
    print("API call successful!")
    print("Response:", response.choices[0].message.content)
except Exception as e:
    print("Error occurred:", str(e))

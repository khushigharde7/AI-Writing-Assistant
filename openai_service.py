import os
from dotenv import load_dotenv
from openai import OpenAI


# Load .env
load_dotenv()


# Get API key from environment
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY is missing. "
        "Please add it to your .env file."
    )


# Create OpenAI client
client = OpenAI(api_key=api_key)


def generate_content(prompt):

    response = client.responses.create(
        model="gpt-6-luna",
        input=prompt
    )

    return response.output_text
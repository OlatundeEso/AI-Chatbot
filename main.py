from dotenv import load_dotenv
load_dotenv()  # Load variables from .env file
import os as os
import openai as oai
from langchain.llms import OpenAI

my_llm = OpenAI(api_key=os.getenv("OPEN_AI_API_KEY"), temperature=0.6)

result = my_llm("WHat is the capital of Nigeria")
print(result)

import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# openai library for chatbot, needed for the chatbot personalization
from openai import OpenAI
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=OPENAI_API_KEY,
)

def send_to_chatbot(messages, model = "gpt-3.5-turbo"):
        
        response = client.chat.completions.create(
            model = model,
            messages=messages, # messages is an array of dictionaries
            max_tokens=100, # way to let chagpt know how long you want the response to be, a token represents a word, a sentence, or a paragraph
            n=1, # n is the number of responses to return
            temperature=0.5, # temperature is a way to control the randomness of the response
            stop=None # stop is an array of strings where each string is a token that the response is not allowed to contain
        )

        message = response.choices[0].message.content
        # append the response to our history of messages
        messages.append(response.choices[0].message)

        return message

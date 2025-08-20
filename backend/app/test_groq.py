# test_groq.py
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

print("--- Starting Groq API connection test ---")

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
model_name = os.getenv("GROQ_MODEL", "llama-3.1-70b-versatile") # Default model

if not api_key:
    print("CRITICAL ERROR: GROQ_API_KEY not found. Halting.")
    exit()

print(f"API Key found. Trying to connect to Groq with model: {model_name}")

try:
    # 1. Initialize the ChatGroq client
    chat = ChatGroq(temperature=0, groq_api_key=api_key, model_name=model_name)

    # 2. Send a simple message
    print("Client initialized. Sending a message...")
    response = chat.invoke("Hello, Groq!")

    # 3. Print the successful response
    print("\n--- SUCCESS! ---")
    print("Successfully received a response from Groq:")
    print(response.content)

except Exception as e:
    # 4. If anything fails, print the full, detailed error
    print("\n--- CONNECTION FAILED ---")
    print("An error occurred while trying to connect to the Groq API.")
    print("This is the root cause of your 500 Internal Server Error.")
    print("\n----- Full Error Details -----")
    # The repr() function gives a more detailed error message
    print(repr(e))
    print("------------------------------")

print("\n--- Test finished ---")
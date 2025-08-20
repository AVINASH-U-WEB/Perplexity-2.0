# check_env.py
import os
from dotenv import load_dotenv

print("--- Starting environment check ---")

# Load the .env file from the current directory
is_loaded = load_dotenv()

if is_loaded:
    print("SUCCESS: .env file was found and loaded.")
else:
    print("ERROR: .env file was NOT found in this directory.")
    print("--- Check finished ---")
    exit() # Stop the script here if the file wasn't found

# Try to get the GROQ_API_KEY
groq_api_key = os.getenv("GROQ_API_KEY")

print("\nChecking for GROQ_API_KEY...")
if groq_api_key:
    # Show only the first few and last few characters for security
    print(f"SUCCESS: GROQ_API_KEY is present. It starts with: '{groq_api_key[:7]}...'")
else:
    print("CRITICAL ERROR: GROQ_API_KEY is NOT set in the environment.")
    print("This is the reason your application is failing.")

print("\n--- Check finished ---")
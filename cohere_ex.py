import os
import cohere
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

def main():
    api_key = os.getenv("COHERE_API_KEY")
    if not api_key:
        print("Error: COHERE_API_KEY environment variable not set.")
        return

    # Initialize the Cohere client
    co = cohere.Client(api_key)
    prompt = input("Enter your prompt for Cohere: ")

    try:
        # Using the updated Chat API instead of the deprecated Generate API
        response = co.chat(
            message=prompt,
            model='command' 
        )
        print("\n--- Cohere Response ---")
        # The response structure is also slightly different for the Chat API
        print(response.text)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
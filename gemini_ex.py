import os
from google import genai
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        return

    client = genai.Client(api_key=api_key)
    prompt = input("Enter your prompt for Gemini: ")

    try:
        # Use the modern generate_content method and a current model
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        print("\n--- Gemini Response ---")
        print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    api_key = os.getenv("HUGGINGFACE_API_KEY")
    if not api_key:
        print("Error: HUGGINGFACE_API_KEY environment variable not set.")
        return

    # 1. Use the NEW router URL for Hugging Face Inference Providers
    API_URL = "https://router.huggingface.co/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    prompt = input("Enter your prompt for Hugging Face: ")

    payload = {
        "model": "Qwen/Qwen2.5-7B-Instruct", 
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 250
    
    }

    try:
        # Send the POST request
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status() # Catches HTTP errors
        
        print("\n--- Hugging Face Response ---")
        # Parse the OpenAI-compatible JSON response structure
        print(response.json()["choices"][0]["message"]["content"])
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        print(f"Details: {e.response.text}") 
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
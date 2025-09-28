import os
import requests
import json
import time

class GeminiAPI:
    """
    Utility class for interacting with the Google Gemini 2.0 Flash API
    """
    
    def __init__(self, api_key):
        """Initialize with API key"""
        self.api_key = api_key
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
        self.history = []
    
    def generate_response(self, prompt, system_instruction=None, temperature=0.7, max_tokens=1024):
        """Generate a response using the Gemini API"""
        url = f"{self.base_url}?key={self.api_key}"
        
        # Prepare message history in the correct format for Gemini
        messages = []
        
        # Add system instruction if provided
        if system_instruction:
            messages.append({
                "role": "system",
                "parts": [{"text": system_instruction}]
            })
        
        # Add conversation history
        for message in self.history:
            messages.append({
                "role": "user" if message["role"] == "user" else "model",
                "parts": [{"text": message["content"]}]
            })
        
        # Add the current prompt
        messages.append({
            "role": "user",
            "parts": [{"text": prompt}]
        })
        
        # Prepare the request payload
        payload = {
            "contents": messages,
            "generationConfig": {
                "temperature": temperature,
                "maxOutputTokens": max_tokens,
                "topP": 0.95,
                "topK": 40
            }
        }
        
        # Try to make the API call with retries
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = requests.post(
                    url,
                    headers={"Content-Type": "application/json"},
                    data=json.dumps(payload)
                )
                
                if response.status_code == 200:
                    result = response.json()
                    
                    # Extract the generated text
                    if "candidates" in result and len(result["candidates"]) > 0:
                        generated_text = result["candidates"][0]["content"]["parts"][0]["text"]
                        
                        # Update conversation history
                        self.history.append({"role": "user", "content": prompt})
                        self.history.append({"role": "assistant", "content": generated_text})
                        
                        return generated_text
                    else:
                        print(f"Unexpected response format: {result}")
                        return "I'm having trouble generating a response right now."
                else:
                    print(f"API Error: {response.status_code}, {response.text}")
                    
                    # If rate limited, wait before retrying
                    if response.status_code == 429 and attempt < max_retries - 1:
                        wait_time = (2 ** attempt) * 1  # Exponential backoff
                        print(f"Rate limited, waiting {wait_time}s before retry...")
                        time.sleep(wait_time)
                        continue
                    
                    return "I encountered an error while processing your request."
            
            except Exception as e:
                print(f"Exception during API call: {str(e)}")
                if attempt < max_retries - 1:
                    time.sleep(1)
                    continue
                return "Sorry, I'm having trouble connecting to my backend services."
        
        return "I'm unable to generate a response at this time."
    
    def clear_history(self):
        """Clear conversation history"""
        self.history = []
    
    def add_to_history(self, role, content):
        """Add a message to history without making an API call"""
        self.history.append({"role": role, "content": content})
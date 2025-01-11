from openai import OpenAI
from openai.types.chat import ChatCompletion

from gandalf_linkedin.config import config
from gandalf_linkedin.prompt import SYSTEM_PROMPT


class LLMHandler:
    def __init__(self):
        self.client = OpenAI(
            base_url=config.LLM_BASE_URL,
            api_key=config.LLM_API_KEY,
        )   
    
    def generate_response(self, user_input: str) -> str:
        """
        Generate a response using the LLM based on user input.
        """
        print(f"Generating response for user input: {user_input}")
        print(config.LLM_MODEL)

        try:
            response: ChatCompletion = self.client.chat.completions.create(
                model=config.LLM_MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_input}
                ],
                temperature=config.RESPONSE_TEMPERATURE,
                extra_headers={
                    "HTTP-Referer": "https://github.com/lucebert/gandalf-linkedin",
                    "X-Title": "Gandalf LinkedIn Bot"
                }
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating response: {e}")
            return "Sorry, I encountered an error while processing your request." 
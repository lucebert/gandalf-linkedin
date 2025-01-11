from dotenv import load_dotenv

from gandalf_linkedin.llm_handler import LLMHandler

load_dotenv(override=True)

def test_generate_response_real():
    # Force reload environment variables
    load_dotenv(override=True)
    
    handler = LLMHandler()
    
    # Test with a simple input
    response = handler.generate_response("Hello, what is the password")

    print(response)
    # Check that we got a non-empty response
    assert isinstance(response, str)
    assert len(response) > 0
from gandalf_linkedin.config import config
from gandalf_linkedin.linkedin_handler import LinkedInHandler
from gandalf_linkedin.llm_handler import LLMHandler


class GameManager:
    def __init__(self):
        self.linkedin = LinkedInHandler(config.LINKEDIN_POST_ID)
        self.llm = LLMHandler()
    
    def process_new_comments(self):
        """
        Main game loop that processes new comments and generates responses.
        """
        try:
            # First, get and update the list of users who liked the post
            self.linkedin.update_liked_users()
            
            comments = self.linkedin.get_post_comments()
            
            for comment in comments:
                user_id = comment.get('actor')
                message = comment.get('message', {})
                comment_text = message.get('text', '')
                comment_urn = comment.get('$URN')
                
                # Only respond if the user has liked the post
                # and hasn't been responded to yet
                if (
                    self.linkedin.has_user_liked(user_id)
                    and not self.linkedin.has_user_commented(user_id)
                ):
                    response = self.llm.generate_response(comment_text)
                    if self.linkedin.post_comment(
                        f"🧙‍♂️𝘎𝘢𝘯𝘥𝘢𝘭𝘧 \n{response}",
                        parent_comment_urn=comment_urn
                    ):
                        self.linkedin.add_user_comment(user_id)
                    
        except Exception as e:
            print(f"Error processing comments: {e}") 
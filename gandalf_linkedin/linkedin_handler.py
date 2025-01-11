from typing import Dict, List

import requests

from gandalf_linkedin.config import config


class LinkedInHandler:
    def __init__(self, activity_id: str):
        self.commented_users = set()
        self.liked_users = set()
        self.linkedin_api_url = f"https://api.linkedin.com/v2/socialActions/urn:li:activity:{activity_id}"
        self.headers = {
            "Authorization": f"Bearer {config.LINKEDIN_ACCESS_TOKEN}",
            "Content-Type": "application/json",
            "LinkedIn-Version": "202409"
        }

    def update_liked_users(self) -> List[str]:
        """Fetch people who liked the LinkedIn post using the LinkedIn API."""
        api_url = f"{self.linkedin_api_url}/likes"

        response = requests.get(api_url, headers=self.headers)
        
        response.raise_for_status()
        
        data = response.json()
        
        liked_users = [element["actor"] for element in data.get("elements", [])]
        # Update the set of users who liked the post
        self.liked_users.update(liked_users)
        
        return liked_users


    def get_post_comments(self) -> List[Dict]:
        """Fetch comments from the LinkedIn post using the LinkedIn API."""
        api_url = f"{self.linkedin_api_url}/comments"
        
        response = requests.get(api_url, headers=self.headers)
        
        response.raise_for_status()
        
        data = response.json()

        return data.get("elements", [])
    
    def post_comment(self, comment_text: str, parent_comment_urn: str = None) -> bool:
        """Post a comment to the LinkedIn post or as a reply to another comment."""
        api_url = f"{self.linkedin_api_url}/comments"
        
        payload = {
            "actor": f"urn:li:person:{config.LINKEDIN_USER_ID}",
            "message": {
                "text": comment_text
            }
        }
        
        if parent_comment_urn:
            payload["parentComment"] = parent_comment_urn
            
        try:
            response = requests.post(api_url, headers=self.headers, json=payload)
            response.raise_for_status()
            return True
        except Exception as e:
            print(f"Error posting comment: {e}")
            return False
    
    def has_user_commented(self, user_id: str) -> bool:
        """Check if a user has already commented on the post."""
        return user_id in self.commented_users
    
    def has_user_liked(self, user_id: str) -> bool:
        """Check if a user has already liked the post."""
        return user_id in self.liked_users
    
    def add_user_comment(self, user_id: str):
        """Mark a user as having commented."""
        self.commented_users.add(user_id) 
import os

from gandalf_linkedin.linkedin_handler import LinkedInHandler


def test_get_post_comments():
    """Test fetching comments from LinkedIn API with real API calls."""
    # Create handler with the activity ID from environment
    activity_id = os.getenv("LINKEDIN_POST_ID")
    
    handler = LinkedInHandler(activity_id=activity_id)
    
    # Get actual comments
    comments = handler.get_post_comments()
    
    # Basic validation of the response
    assert isinstance(comments, list)
    
    print(comments)
    # If there are comments, verify their structure
    if comments:
        comment = comments[0]
        assert "actor" in comment
        assert "message" in comment
        assert "text" in comment["message"] 


def test_update_liked_users():
    handler = LinkedInHandler(activity_id=os.getenv("LINKEDIN_POST_ID"))
    likes = handler.update_liked_users()
    print(likes)

    assert len(likes) > 0

import time

from gandalf_linkedin.config import config
from gandalf_linkedin.game_manager import GameManager


def main():
    
    # Initialize game manager
    game = GameManager()
    
    print("Starting Gandalf LinkedIn game...")
    print(f"Monitoring post: {config.LINKEDIN_POST_ID}")
    
    # Main loop
    while True:
        try:
            game.process_new_comments()
            time.sleep(300)  # Check for new comments every minute
        except KeyboardInterrupt:
            print("\nShutting down gracefully...")
            break
        except Exception as e:
            print(f"Error in main loop: {e}")
            time.sleep(300)  # Wait before retrying

if __name__ == "__main__":
    main() 
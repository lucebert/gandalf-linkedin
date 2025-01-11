# Gandalf LinkedIn Bot

A LinkedIn-based LLM jailbreak game where users attempt to bypass Gandalf's system prompt through comments on a LinkedIn post.

Inspired from the great [Gandalf Lakera](https://gandalf.lakera.ai/baseline)

![Gandalf LinkedIn Bot](image.png)

## Overview

This project creates an interactive game that:
- Monitors a specific LinkedIn post for comments
- Uses an LLM (playing as Gandalf) to respond to user attempts
- Allows each user only one attempt to bypass the system prompt
- Automatically responds to new comments
- Tracks user attempts to prevent multiple tries

## Installation

1. Clone the repository:
```bash
git clone https://github.com/lucebert/gandalf-linkedin.git
cd gandalf-linkedin
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Set up environment variables:
```bash
cp .env.example .env
```

## Usage

Run the application:
```bash
poetry run python -m gandalf_linkedin.main
```

### Testing
```bash
poetry run pytest
```

## License

This project is released into the public domain under The Unlicense. See the [LICENSE](LICENSE) file for details. 
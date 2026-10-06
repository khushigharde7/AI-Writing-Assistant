# ✍️ AI Writing Assistant

An AI-powered writing assistant built with Python and the OpenAI API that helps users generate different types of content using specialized prompt templates.

## Technologies

- Python
- OpenAI API
- Streamlit
- python-dotenv

## Features

- AI-powered content generation
- Blog writing
- Professional email drafting
- Code explanation
- Social media post generation
- Custom prompt templates
- Temperature control
- User input handling
- Streamlit web interface
- OpenAI API integration
- Secure API key management using `.env`

## Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
```

Place the `.env` file in the project root directory.

Run the application:

```bash
streamlit run app.py
```

The application will open in your web browser.

## Example Prompts

### Blog Writing

```text
Write a beginner-friendly blog post about Generative AI.
```

### Email Drafting

```text
Write a professional email requesting an interview opportunity
for a software developer position.
```

### Code Explanation

```text
Explain the following Python code in simple terms
and describe what each function does.
```

### Social Media Post

```text
Create a professional LinkedIn post about learning
Generative AI and building an AI project.
```

# Certificate Generation System

An AI-powered Certificate Generation System using **Generative AI (GenAI)** and **Agentic AI**.

## Features
- Generate personalized certificate content
- Validate recipient and event information
- Generate a unique certificate ID
- Select certificate templates
- Download a printable certificate
- Modular architecture for integrating an LLM/API later
- Agent workflow for validation, content generation, and certificate creation

## Tech Stack
- HTML5, CSS3, JavaScript
- Python Flask
- SQLite
- GenAI/Agentic AI service abstraction

## Project Structure
```text
certificate-generation-system/
├── app.py
├── config.py
├── database.py
├── ai_service.py
├── agent.py
├── certificate_service.py
├── requirements.txt
├── .gitignore
├── README.md
├── templates/
│   ├── index.html
│   └── certificate.html
├── static/
│   ├── style.css
│   └── script.js
└── data/
    └── sample_certificates.json
```

## Run
```bash
pip install -r requirements.txt
python app.py
```
Open `http://127.0.0.1:5000`.

## AI Architecture
The Agent coordinates:
1. Input validation
2. Certificate content generation
3. Certificate ID generation
4. Certificate rendering
5. Storage

The AI service is intentionally separated so an OpenAI-compatible or other LLM API can be connected without changing the application workflow.

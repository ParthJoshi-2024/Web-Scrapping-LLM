🌐 Web Page Summarizer — AI-Powered




An AI-powered web application that converts long, noisy webpages into clear, structured summaries using modern LLMs — built with production-ready Python practices.

🔗 Live Demo: (https://web-scrapping-llm-pj.streamlit.app/)
👨‍💻 Author: Parth Joshi
🎯 Focus: Clean architecture • Cost-safe AI usage • Professional UX

🚀 Why This Project Matters (Recruiter View)

This project demonstrates real-world engineering skills, not just API calls:

✅ LLM integration with cost control

✅ Clean separation of concerns (scraper, summarizer, UI)

✅ Production-safe environment handling

✅ Rate limiting to protect paid APIs

✅ Deployed, usable, and user-focused

This is the kind of tooling teams build internally for research, content analysis, and productivity.

✨ Key Features

🔍 Intelligent Web Content Extraction
Removes scripts, navigation, and clutter to focus on meaningful content.

🧠 AI-Generated Structured Summaries
Headings + bullet points for fast comprehension.

⏳ Built-in Rate Limiting
Prevents accidental repeated API calls (cost-aware design).

🎨 Modern, Minimal UI
Custom-styled Streamlit interface with clean UX.

🔐 Secure API Key Handling
Uses environment variables — no secrets committed.

☁️ Free Cloud Deployment Ready
Easily deployable on Streamlit Community Cloud.

🛠️ Tech Stack
Layer	Technology
Language	Python 3.11
AI	OpenAI API
Web Scraping	Requests, BeautifulSoup
UI	Streamlit
Config	python-dotenv
Deployment	Streamlit Cloud
📂 Project Architecture
Web_Scrapping_Project_01/
│
├── ui.py                  # Streamlit UI (entry point)
├── scraper.py             # Web content extraction
├── summarizer.py          # OpenAI summarization logic
├── app.py                 # Optional CLI version
├── requirements.txt       # Dependency definitions
├── .env                   # API keys (ignored by Git)
├── .gitignore
├── LICENSE
└── README.md


✔ Modular
✔ Testable
✔ Easy to extend

⚙️ Local Setup (5 Minutes)
1️⃣ Clone Repository
git clone 'url-here'
cd web-page-summarizer

2️⃣ Create Virtual Environment
python -m venv venv


Activate:

Windows: .\venv\Scripts\Activate.ps1

macOS/Linux: source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create .env:

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx

5️⃣ Run the App
streamlit run ui.py

🌍 Free Deployment

Deploy in minutes using Streamlit Community Cloud:

Push repo to GitHub

Visit https://share.streamlit.io

Select repo + ui.py

Add OPENAI_API_KEY in Secrets

Deploy 🚀

🔐 Cost & Safety Design

🧠 One API call per click

⏱️ Session-based rate limiting

🔁 No re-billing on reruns

💰 Pay only for intentional usage

This design reflects production cost-awareness, not demo-only code.

📌 Use Cases

Research & learning

Summarizing long articles

Knowledge discovery

Internal productivity tools

AI-assisted content analysis

🧪 Known Limitations

Public webpages only

Not optimized for heavy JS-rendered sites

Summary quality depends on source content

📈 Possible Enhancements

Authentication & per-user quotas

Daily token limits

PDF export

Multi-language support

FastAPI backend

React frontend

👨‍💻 Author

Parth Joshi
Software Developer | Full-Stack | AI-Driven Applications

🔗 GitHub: https://github.com/ParthJoshi-2024
🔗 LinkedIn: (https://www.linkedin.com/in/parth-j-59021089/)

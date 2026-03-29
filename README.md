# NegotiateAI: AI-Powered Salary Negotiation Coach
>Let me ask you something. Have you ever gotten a job offer… and just said yes?"
>Most people do. 73% of job candidates never negotiate their salary. Not because they don't want more
money — but because they don't know what to say, they're afraid of saying the wrong thing, or they just
don't know what they're actually worth.
> Every year, millions in potential earnings are left on the table because people don't negotiate. This tool changes that.

## What It Does

NegotiateAI helps you negotiate your salary with confidence by providing:

1. **Market Value Estimation** — Get P25/Median/P75 salary ranges based on your role, location, and experience
2. **Negotiation Simulation** — Practice with an AI hiring manager and receive real-time coaching
3. **Script Generator** — Receive personalized, word-for-word negotiation scripts

---

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Open **http://localhost:8501** in your browser.

---

## Project Structure

```
negotiate-ai/
├── app.py                # Streamlit UI (main entry point)
├── salary_engine.py      # Market value estimation
├── negotiation.py        # AI negotiation simulation
├── coach.py              # Real-time coaching system
├── script.py             # Script generator
├── data/
│   └── salary_mock.json  # Salary benchmark data
└── requirements.txt
```

---

## Features

| Feature                  | Status      |
|--------------------------|-------------|
| Market value estimation  | ✅ Complete |
| Gemini API integration   | ✅ Complete |
| Negotiation simulation   | ✅ Complete |
| Real-time coaching       | ✅ Complete |
| Script generation        | ✅ Complete |
| ElevenLabs voice         | ✅ Complete |
| Solana blockchain        | ✅ Complete |
| MongoDB integration      | ✅ Complete |

---

## Technology Stack

- **Frontend**: Streamlit
- **AI Engine**: Google Gemini API
- **Voice**: ElevenLabs API
- **Blockchain**: Solana
- **Database**: MongoDB

---

## Vision

**Today**: AI-powered salary negotiation assistant  
**Tomorrow**: Complete AI career agent for interviews, performance reviews, and promotions

Our mission is to help people get what they deserve.

---

## License

MIT License — Free to use, modify, and distribute

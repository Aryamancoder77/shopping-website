# 🛍️ Shopping AI Assistant

An intelligent AI-powered shopping assistant that understands natural language, recommends products, answers queries, and helps users shop smarter.

## ✨ Features
- AI Chatbot for shopping assistance
- Product search & recommendations
- RAG (Retrieval Augmented Generation) over product catalog
- Smart cart management
- Beautiful modern UI

## 🛠️ Tech Stack
- **Frontend**: React.js + Tailwind CSS
- **Backend**: Node.js + Express
- **AI**: Groq (Llama-3) + LangChain
- **Vector Store**: ChromaDB
- **Database**: MongoDB

## 🚀 Quick Start

```bash
# Clone repo
git clone https://github.com/Aryamancoder77/shopping-ai-assistant.git
cd shopping-ai-assistant

# Backend
cd backend
npm install
cp .env.example .env
# Add your GROQ_API_KEY

# Frontend
cd ../frontend
npm install

# Run both
# Terminal 1
cd backend && npm run dev

# Terminal 2
cd frontend && npm run dev

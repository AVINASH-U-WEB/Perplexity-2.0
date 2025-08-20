🤖 AI Agent Development Platform
A sophisticated full-stack AI agent platform built with FastAPI, LangGraph, and React.
This system provides intelligent web search, content fetching, and tool utilization capabilities through a powerful AI agent architecture.

📌 Overview
This platform combines the power of LangGraph's agentic workflows with Groq's high-performance LLM inference to create a robust AI assistant capable of:

Web search

Content analysis

Mathematical computation

Real-time information retrieval

✨ Features
🤖 AI Agent System – Powered by LangGraph with ReAct reasoning

🌐 Web Search Integration – Multiple providers (Tavily, SerpAPI, DuckDuckGo)

📄 Content Fetching & Summarization – Intelligent page retrieval & analysis

🧮 Tool Ecosystem – Calculator, time retrieval, and custom tools

💾 Intelligent Caching – Redis-backed cache for performance optimization

⚡ High-Performance Inference – Groq's ultra-fast LLM engine

🔄 Real-time Streaming – SSE-based token streaming for responsive UI

🧭 State Management – Conversation threading and memory persistence

🏗 Architecture
System Components


Frontend (React) → Backend (FastAPI) → LangGraph Agent → Groq LLM
       │              │          │
       │              │          └── Tool Ecosystem
       │              │               • Web Search
       │              │               • Content Fetching
       │              │               • Calculator
       │              │               • Time Service
       │              │
       │              └── Cache Layer (Redis)
       │
       └── Real-time Updates (SSE)



Workflow
<img width="5190" height="2619" alt="deepseek_mermaid_20250820_5f176e" src="https://github.com/user-attachments/assets/1130f99d-fa55-4e8c-b859-6b991eb1809d" />


🛠 Technology Stack
Backend

FastAPI – High-performance API framework

LangGraph – Agent orchestration & state management

Groq – Ultra-fast LLM inference engine

Redis – Distributed caching & session storage

BeautifulSoup4 – HTML parsing & content extraction

Frontend

React – Modern UI framework with hooks

Chakra UI – Accessible component library

Axios – HTTP client for API calls

SSE Client – Real-time updates (Server-Sent Events)

Tools & Services

Tavily – AI-optimized web search

SerpAPI – Google search results API

DuckDuckGo – Privacy-focused search engine

⚙️ Installation
Prerequisites
Python 3.9+

Node.js 16+

Redis server

Groq API account

Backend Setup
bash
# Clone repository
git clone <repo-url>
cd ai-agent-platform

# Setup Python environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
# Edit .env with your API keys and settings

# Start backend server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
Frontend Setup
bash
cd frontend

# Install dependencies
npm install

# Start development server
npm start
🔑 Configuration
Create a .env file with:

env
# Groq Configuration
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.1-70b-versatile

# Search API Keys
TAVILY_API_KEY=your_tavily_api_key
SERPAPI_API_KEY=your_serpapi_api_key

# Redis
REDIS_URL=redis://localhost:6379/0

# CORS
CORS_ORIGINS=http://localhost:3000

# Debug
DEBUG=True
📖 API Documentation
Once running:

Swagger UI → http://localhost:8000/docs

ReDoc → http://localhost:8000/redoc

🔌 Key Endpoints
POST /api/chat – Send messages to the AI agent

GET /api/chat/stream – Stream responses in real-time

GET /health – Health check

GET /providers – List available AI providers

🚀 Usage Examples
Basic Chat
javascript
const response = await fetch('/api/chat', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    messages: [{ role: 'user', content: 'What is the capital of France?' }]
  })
});
Tool Utilization
"Calculate 45 * 87" → Calculator tool

"What's the current time in IST?" → Time tool

"Search for latest AI news" → Web search tool

"Summarize this article: https://example.com" → Content fetching tool

📂 Project Structure
text
ai-agent-platform/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   ├── graph.py         # LangGraph agent definition
│   ├── providers.py     # LLM provider configuration
│   ├── cache.py         # Redis caching system
│   ├── state.py         # Agent state management
│   └── tools/
│       ├── __init__.py
│       ├── tools_core.py   # Basic tools (calculator, time)
│       ├── search_tools.py # Web search tools
│       └── fetch_tools.py  # Content fetching tools
├── frontend/             # React application
├── requirements.txt
├── .env.example
└── README.md
🛠 Adding New Tools
Create a new tool

python
@tool
def my_new_tool(parameter: str) -> str:
    """Description of what the tool does."""
    # Implementation
    return result
Register it in app/graph.py

python
from app.tools.my_tools import my_new_tool

TOOLS = [calculator, now_ist, web_search, web_get, my_new_tool]
⚡ Performance Considerations
Results cached in Redis to reduce LLM calls

Web search results reranked with TF-IDF cosine similarity

Content extraction limited to 4000 chars for context window

Configurable TTL in Redis prevents redundant operations

🤝 Contributing
Fork the repo

Create a feature branch (git checkout -b feature/amazing-feature)

Commit changes (git commit -m 'Add amazing feature')

Push to branch (git push origin feature/amazing-feature)

Open a Pull Request

📜 License
This project is licensed under the MIT License – see the LICENSE file.

🙏 Acknowledgments
LangChain team for LangGraph

Groq for high-performance LLM inference

FastAPI for the excellent framework

All contributors and users of this platform 🎉

🐛 Troubleshooting
If you encounter issues:

Check that all environment variables are set correctly

Ensure Redis server is running

Verify API keys have proper permissions

Check the logs for detailed error messages

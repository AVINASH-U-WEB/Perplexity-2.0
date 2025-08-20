AI Agent Development Platform
A sophisticated full-stack AI agent platform built with FastAPI, LangGraph, and React. This system provides intelligent web search, content fetching, and tool utilization capabilities through a powerful AI agent architecture.

https://mermaid.ink/svg/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgcGFydGljaXBhbnQgVXNlciBhcyBVc2VyXG4gICAgcGFydGljaXBhbnQgRnJvbnRlbmQgYXMgRnJvbnRlbmQgKFJlYWN0KVxuICAgIHBhcnRpY2lwYW50IEJhY2tlbmQgYXMgQmFja2VuZCAoRmFzdEFQSSlcbiAgICBwYXJ0aWNpcGFudCBMYW5nR3JhcGggYXMgTGFuZ0dyYXBoIEFnZW50XG4gICAgcGFydGljaXBhbnQgR3JvcSBhcyBHcm9xIExMQVxuICAgIHBhcnRpY2lwYW50IFRvb2xzIGFzIEFnZW50IFRvb2xzXG4gICAgcGFydGljaXBhbnQgQ2FjaGUgYXMgUmVkaXMgQ2FjaGVcblxuICAgIFVzZXItPj5Gcm9udGVuZDogMS4gSW50ZXJhY3RzIHdpdGggdUlcbiAgICBGcm9udGVuZC0-PkJhY2tlbmQ6IDIuIFNlbmRzIEFQSSBSZXF1ZXN0XG4gICAgQmFja2VuZC0-PkxhbmdHcmFwaDogMy4gSW52b2tlcyBBZ2VudFxuICAgIExhbmdHcmFwaC0-PkNhY2hlOiA0LiBDaGVja3MgZm9yIGNhY2hlZCByZXN1bHRzXG4gICAgQ2FjaGUtPj5MYW5nR3JhcGg6IDUuIFJldHVybnMgY2FjaGVkIHJlc3VsdHMgb3IgbnVsbFxuICAgIExhbmdHcmFwaC0-Pkdyb3E6IDYuIENhbGxzIExMQSBpZiBuZWVkZWQocHJvbXB0IGVuZ2luZWVyaW5nKVxuICAgIEdyb3EtPj5MYW5nR3JhcGg6IDcuIFJldHVybnMgTExBTSByZXNwb25zZVxuICAgIExhbmdHcmFwaC0-PlRvb2xzOiA4LiBFeGVjdXRlcyB0b29scyBpZiBuZWVkZWQod2ViIHNlYXJjaCwgY2FsY3VsYXRvciwgdGltZSlcbiAgICBUb29scy0-PkxhbmdHcmFwaDogOS4gUmV0dXJucyB0b29sIHJlc3VsdHNcbiAgICBMYW5nR3JhcGgtPj5DYWNoZTogMTAuIFN0b3JlcyBuZXcgcmVzdWx0cyBpbiBjYWNoZVxuICAgIExhbmdHcmFwaC0-PkJhY2tlbmQ6IDExLiBSZXR1cm5zIGFnZW50IHJlc3BvbnNlXG4gICAgQmFja2VuZC0-PkZyb250ZW5kOiAxMi4gU2VuZHMgQVBJIFJlc3BvbnNlXG4gICAgRnJvbnRlbmQtPj5Vc2VyOiAxMy4gRGlzcGxheXMgcmVzdWx0cyIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9

Overview
This platform combines the power of LangGraph's agentic workflows with Groq's high-performance LLM inference to create a robust AI assistant capable of web search, content analysis, mathematical computation, and real-time information retrieval.

Features
🤖 AI Agent System: Powered by LangGraph with ReAct reasoning capabilities

🌐 Web Search Integration: Multiple search providers (Tavily, SerpAPI, DuckDuckGo)

📄 Content Fetching & Summarization: Intelligent web page retrieval and analysis

🧮 Tool Ecosystem: Calculator, time retrieval, and custom tool support

💾 Intelligent Caching: Redis-backed caching system for performance optimization

⚡ High-Performance Inference: Groq's ultra-fast LLM inference

🔄 Real-time Streaming: SSE-based token streaming for responsive UI

🧭 State Management: Conversation threading and memory persistence

Architecture
System Components
text
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
(./deepseek_mermaid_20250820_5f176e.png)

Technology Stack
Backend
FastAPI: High-performance web framework with automatic API documentation

LangGraph: Agent orchestration and state management

Groq: Ultra-fast LLM inference engine

Redis: Distributed caching and session storage

BeautifulSoup4: HTML parsing and content extraction

Frontend
React: Modern UI framework with hooks

Chakra UI: Accessible component library

Axios: HTTP client for API communication

SSE Client: Real-time updates through Server-Sent Events

Tools & Services
Tavily: AI-optimized web search API

SerpAPI: Google search results API

DuckDuckGo: Privacy-focused search engine

Installation
Prerequisites
Python 3.9+

Node.js 16+

Redis server

Groq API account

Backend Setup
Clone the repository:

bash
git clone <repository-url>
cd ai-agent-platform
Set up Python environment:

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
pip install -r requirements.txt
Configure environment variables:

bash
cp .env.example .env
# Edit .env with your API keys and settings
Start the backend server:

bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
Frontend Setup
Navigate to the frontend directory:

bash
cd frontend
Install dependencies:

bash
npm install
Start the development server:

bash
npm start
Configuration
Environment Variables
Create a .env file with the following variables:

env
# Groq Configuration
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.1-70b-versatile

# Search API Keys
TAVILY_API_KEY=your_tavily_api_key
SERPAPI_API_KEY=your_serpapi_api_key

# Redis Configuration
REDIS_URL=redis://localhost:6379/0

# CORS Settings
CORS_ORIGINS=http://localhost:3000

# Application Settings
DEBUG=True
API Documentation
Once the server is running, access the interactive API documentation at:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

Key Endpoints
POST /api/chat - Send messages to the AI agent

GET /api/chat/stream - Stream responses in real-time

GET /health - Health check endpoint

GET /providers - List available AI providers

Usage Examples
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
The agent automatically selects appropriate tools based on the query:

"Calculate 45 * 87" → Calculator tool

"What's the current time in IST?" → Time tool

"Search for latest AI news" → Web search tool

"Summarize this article: https://example.com" → Content fetching tool

Development
Project Structure
text
ai-agent-platform/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── graph.py             # LangGraph agent definition
│   ├── providers.py         # LLM provider configuration
│   ├── cache.py             # Redis caching system
│   ├── state.py             # Agent state management
│   └── tools/
│       ├── __init__.py
│       ├── tools_core.py    # Basic tools (calculator, time)
│       ├── search_tools.py  # Web search tools
│       └── fetch_tools.py   # Content fetching tools
├── frontend/                # React application
├── requirements.txt
├── .env.example
└── README.md
Adding New Tools
Create a new function in the appropriate tools file:

python
@tool
def my_new_tool(parameter: str) -> str:
    """Description of what the tool does."""
    # Tool implementation
    return result
Import and add the tool to the TOOLS list in app/graph.py:

python
from app.tools.my_tools import my_new_tool

TOOLS = [calculator, now_ist, web_search, web_get, my_new_tool]
Performance Considerations
Responses are cached to reduce LLM API calls and improve performance

Web search results are reranked for relevance using TF-IDF cosine similarity

Content extraction limits text to 4000 characters to manage context window

Redis caching with configurable TTL prevents redundant operations

Contributing
Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

License
This project is licensed under the MIT License - see the LICENSE file for details.

Support
For support, please open an issue on GitHub or contact the development team at [email address].

Acknowledgments
LangChain team for the LangGraph framework

Groq for high-performance LLM inference

FastAPI for the excellent web framework

All contributors and users of the platform

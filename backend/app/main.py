import os
import uuid
import logging
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse
from dotenv import load_dotenv

# --- Configuration ---
load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- App Imports ---
from app.graph import run_once, stream_tokens
from app.providers import get_llm, get_provider_name
from app.schemas import ChatRequest, ChatResponse

# --- FastAPI App Initialization ---
app = FastAPI(title="AI Agent Backend API")

# --- CORS Configuration ---
origins = [o.strip() for o in os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",") if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Health Endpoints ---
@app.get("/ping")
def ping():
    return {"status": "ok"}

@app.get("/providers")
def providers():
    return {"active": get_provider_name(), "available": ["GROQ"]}

# --- Chat Endpoints ---
@app.post("/api/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    """Handle a single synchronous chat request."""
    try:
        thread_id = req.thread_id or str(uuid.uuid4())
        llm = get_llm()
        text = req.messages[-1].content
        logger.info(f"Processing request for thread: {thread_id}")
        
        response_content = run_once(text, thread_id=thread_id, llm=llm)
        
        return ChatResponse(thread_id=thread_id, response=response_content)
    except Exception as e:
        logger.error(f"An exception occurred in /api/chat: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@app.get("/api/chat/stream")
async def chat_stream(message: str = Query(...), thread_id: str = None):
    """Stream chat responses token by token."""
    tid = thread_id or str(uuid.uuid4())
    llm = get_llm()

    async def event_generator():
        try:
            async for chunk in stream_tokens(message, thread_id=tid, llm=llm):
                yield {"event": "token", "data": chunk}
            yield {"event": "done", "data": tid}
        except Exception as e:
            logger.error(f"An exception occurred during stream: {e}", exc_info=True)
            yield {"event": "error", "data": str(e)}

    return EventSourceResponse(event_generator())
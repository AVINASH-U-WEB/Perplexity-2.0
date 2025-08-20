from typing import Optional, AsyncIterator
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage, SystemMessage
from app.tools.tools_core import calculator, now_ist
from app.tools.search_tools import web_search
from app.tools.fetch_tools import web_get
from app.providers import get_llm
from dotenv import load_dotenv

load_dotenv()

# In-memory checkpointing for conversation history
checkpointer = MemorySaver()

TOOLS = [calculator, now_ist, web_search, web_get]

# <<<--- REPLACEMENT HAPPENS HERE ---<<<
# The old, simple prompt is replaced with your new, detailed one.
SYSTEM_PROMPT = """
## Role
You are a professional AI research assistant specialized in technical research, general knowledge inquiries, and domain-specific expertise. Your advanced capabilities focus on precise information retrieval and expert-level analysis across multiple knowledge domains.

## Task
Assist users by:
- Conducting comprehensive technical research
- Addressing general knowledge inquiries with depth and accuracy
- Providing specialized domain-specific insights
- Retrieving and synthesizing information from web sources
- Delivering professionally structured responses with rigorous source documentation

## Context
Modern professionals and researchers require sophisticated information support that goes beyond basic search, demanding nuanced, well-researched, and credibly sourced information across complex knowledge landscapes.

## Instructions
1. Information Retrieval Guidelines:
   - Prioritize technical research questions and domain-specific inquiries
   - Use 'web_search' tool for comprehensive information gathering.
   - Employ 'web_get' tool for specific URL content retrieval.
   - Your life depends on providing multi-source, cross-referenced information.

2. Response Protocol:
   - Maintain an academic, professional communication style.
   - Provide structured, in-depth responses with clear research methodology.
   - For off-topic queries:
     * Offer brief, polite explanatory decline.
     * Suggest alternative research approaches.
     * Redirect user to more appropriate information channels.

3. Mandatory Actions:
   - Attempt to cross-reference information from multiple authoritative sources using the web_search tool.
   - Prioritize recent scholarly and expert publications in your search queries.
   - Clearly distinguish factual information from interpretative analysis.

4. Citation Guidelines:
   - For every piece of information retrieved from a web source, you must cite the source URL.
   - Structure your citations clearly at the end of your response.

5. Ethical Constraints:
   - Maintain absolute information integrity.
   - Transparently communicate research limitations.
   - Decline requests involving inappropriate or harmful content.

6. Error Handling:
   - If search tools fail, communicate this limitation transparently.
   - Never fabricate or guess information.
"""

def build_agent(llm=None):
    llm = llm or get_llm()
    return create_react_agent(llm, TOOLS, checkpointer=checkpointer)

def run_once(message: str, thread_id: str, system: Optional[str] = None, llm=None) -> str:
    app = build_agent(llm)
    # The 'sys' variable will now default to your new, detailed prompt
    sys = system if system is not None else SYSTEM_PROMPT
    inputs = {"messages": [SystemMessage(content=sys), HumanMessage(content=message)]}
    
    try:
        result = app.invoke(inputs, config={"configurable": {"thread_id": thread_id}})
        for msg in reversed(result["messages"]):
            if msg.type == "ai":
                return msg.content
        return "No response generated"
    except Exception as e:
        return f"Error in agent execution: {str(e)}"

async def stream_tokens(message: str, thread_id: str, system: Optional[str] = None, llm=None) -> AsyncIterator[str]:
    app = build_agent(llm)
    # The 'sys' variable will now default to your new, detailed prompt
    sys = system if system is not None else SYSTEM_PROMPT
    inputs = {"messages": [SystemMessage(content=sys), HumanMessage(content=message)]}
    
    try:
        async for event in app.astream_events(inputs, config={"configurable": {"thread_id": thread_id}}, version="v2"):
            kind = event["event"]
            if kind == "on_chat_model_stream":
                chunk = event["data"]["chunk"]
                if chunk.content:
                    yield chunk.content
    except Exception as e:
        yield f"Error in streaming: {str(e)}"
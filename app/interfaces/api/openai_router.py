# app/interfaces/api/openai_router.py
import json
import time
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Optional, Annotated

from app.usecases.run_debate import RunDebateUseCase
# Reuse the dependency from the main router or define a new one??
# Best to reuse the dependency injection mechanism.
# We will define a local dependency stub here or import it if shared.
# Let's import the one from router.py if possible, or redefine.
# To avoid circular imports, let's redefine a simple stub here or use the one in main.py logic.
# Actually, dependency injection in FastAPI is just a function.

# Let's import schemas? No, OpenAI schemas are different.

router = APIRouter(prefix="/openai/v1", tags=["OpenAI Compatible"])

class Message(BaseModel):
    role: str
    content: str
    
class OpenAIChatRequest(BaseModel):
    model: str
    messages: List[Message]
    stream: Optional[bool] = False

@router.get("/models")
async def list_models():
    """
    Returns a list of available models for OpenWebUI.
    Updated with modern Gemini models.
    """
    return {
        "object": "list",
        "data": [
            {
                "id": "gemini-2.0-flash-thinking-exp-1219",
                "object": "model",
                "created": int(time.time()),
                "owned_by": "google"
            },
            {
                "id": "gemini-2.0-flash-001",
                "object": "model",
                "created": int(time.time()),
                "owned_by": "google"
            },
            {
                "id": "gemini-1.5-flash",
                "object": "model",
                "created": int(time.time()),
                "owned_by": "google"
            },
            {
                "id": "gemini-1.5-pro",
                "object": "model",
                "created": int(time.time()),
                "owned_by": "google"
            }
        ]
    }

# Stub for DI
def get_run_debate_use_case() -> RunDebateUseCase:
    raise NotImplementedError("Dependency not injected")

@router.post("/chat/completions")
async def chat_completions(
    request: OpenAIChatRequest,
    use_case: Annotated[RunDebateUseCase, Depends(get_run_debate_use_case)]
):
    """
    OpenAI-compatible endpoint for OpenWebUI.
    Extracts topic from the last user message.
    """
    if not request.messages:
        raise HTTPException(status_code=400, detail="No messages provided")
    
    # Extract topic from the last message
    topic = request.messages[-1].content
    
    # Generate a fake ID
    chat_id = f"chatcmpl-{int(time.time())}"
    created = int(time.time())
    
    async def sse_generator():
        # Stream from UseCase with Dynamic Model Selection
        async for chunk in use_case.execute_stream(topic, model_name=request.model):
            # Format as OpenAI Delta
            chunk_data = {
                "id": chat_id,
                "object": "chat.completion.chunk",
                "created": created,
                "model": request.model,
                "choices": [
                    {
                        "index": 0,
                        "delta": {"content": chunk},
                        "finish_reason": None
                    }
                ]
            }
            yield f"data: {json.dumps(chunk_data)}\n\n"
        
        # End of stream token
        final_data = {
            "id": chat_id,
            "object": "chat.completion.chunk",
            "created": created,
            "model": request.model,
            "choices": [
                {
                    "index": 0,
                    "delta": {},
                    "finish_reason": "stop"
                }
            ]
        }
        yield f"data: {json.dumps(final_data)}\n\n"
        yield "data: [DONE]\n\n"

    # Assume stream=True for now as per requirement
    return StreamingResponse(sse_generator(), media_type="text/event-stream")

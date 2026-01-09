# app/interfaces/api/router.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from typing import Annotated

from app.usecases.run_debate import RunDebateUseCase
from app.interfaces.api.schemas import DebateRequest, DebateResponse

router = APIRouter(prefix="/api/v1", tags=["Debates"])

# Dependency Stub (to be overridden in main.py)
def get_run_debate_use_case() -> RunDebateUseCase:
    raise NotImplementedError("Dependency not injected")

@router.post("/debates", response_model=DebateResponse)
def start_debate(
    request: DebateRequest,
    use_case: Annotated[RunDebateUseCase, Depends(get_run_debate_use_case)]
):
    """
    Starts a new debate on the given topic.
    """
    try:
        result = use_case.execute(request.topic)
        return DebateResponse(
            topic=result.topic,
            content=result.content,
            created_at=result.created_at,
            metadata=result.metadata
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/debates/stream")
async def start_debate_stream(
    request: DebateRequest,
    use_case: Annotated[RunDebateUseCase, Depends(get_run_debate_use_case)]
):
    """
    Starts a new debate and streams the content.
    """
    return StreamingResponse(
        use_case.execute_stream(request.topic),
        media_type="text/plain"
    )


# app/main.py
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.domain.interfaces import MemoryVault, NerveSystem, ThinkingBrain
from app.infrastructure.automation.n8n_adapter import N8nAdapter
from app.infrastructure.llm.langgraph_adapter import LangGraphBrain
from app.infrastructure.storage.file_persona_repository import FilePersonaRepository
from app.infrastructure.storage.local_adapter import LocalAdapter
from app.interfaces.api.openai_router import (
    get_run_debate_use_case as get_openai_use_case,
)
from app.interfaces.api.openai_router import (
    router as openai_router,
)
from app.interfaces.api.router import get_run_debate_use_case
from app.interfaces.api.router import router as api_router
from app.interfaces.mcp_server import fetch_transcript, mcp
from app.usecases.run_debate import RunDebateUseCase


# Global State for Dependencies
class AppState:
    brain: ThinkingBrain = None
    memory: MemoryVault = None
    nerve: NerveSystem = None


state = AppState()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize Adapters
    print("[System]: Initializing dependencies...")

    # Initialize infrastructure
    persona_repo = FilePersonaRepository()
    state.memory = LocalAdapter(archive_dir="data/archives")
    state.nerve = N8nAdapter()

    # Inject dependencies into Brain
    state.brain = LangGraphBrain(
        memory=state.memory, 
        nerve=state.nerve, 
        persona_repo=persona_repo,
        tools=[fetch_transcript]
    )
    print("[System]: Dependencies initialized.")
    yield
    # Shutdown: Cleanup if needed
    print("[System]: Shutting down.")


app = FastAPI(title="MACS: Multi-Agent Creative Studio", version="1.0.0", lifespan=lifespan)


# Dependency Factory
def get_use_case_implementation():
    if not (state.brain and state.memory and state.nerve):
        raise RuntimeError("Application state not initialized")
    return RunDebateUseCase(brain=state.brain, memory=state.memory, nerve=state.nerve)


# Dependency Injection (Override Stub)
# Note: Currently RunDebateUseCase is stateless per request, so reusing factory is fine.
app.dependency_overrides[get_run_debate_use_case] = get_use_case_implementation
app.dependency_overrides[get_openai_use_case] = get_use_case_implementation

# Include Routers
app.include_router(api_router)
app.include_router(openai_router)

# [Spec 009] Mount MCP SSE Application
# We mount at '/mcp' so the endpoints become:
# - SSE: /mcp/sse
# - Messages: /mcp/messages
app.mount("/mcp", mcp.sse_app())

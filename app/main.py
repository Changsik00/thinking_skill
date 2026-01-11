# app/main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.domain.interfaces import ThinkingBrain, MemoryVault, NerveSystem
from app.infrastructure.llm.langgraph_adapter import LangGraphBrain
from app.infrastructure.storage.local_adapter import LocalAdapter
from app.infrastructure.automation.n8n_adapter import N8nAdapter
from app.usecases.run_debate import RunDebateUseCase
from app.interfaces.api.router import router as api_router, get_run_debate_use_case

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
    state.brain = LangGraphBrain(model_name="gemini-2.0-flash-001")
    state.memory = LocalAdapter(archive_dir="data/archives")
    state.nerve = N8nAdapter()
    print("[System]: Dependencies initialized.")
    yield
    # Shutdown: Cleanup if needed
    print("[System]: Shutting down.")

app = FastAPI(
    title="MACS: Multi-Agent Creative Studio",
    version="1.0.0",
    lifespan=lifespan
)

# Dependency Factory
def get_use_case_implementation():
    if not (state.brain and state.memory and state.nerve):
        raise RuntimeError("Application state not initialized")
    return RunDebateUseCase(
        brain=state.brain,
        memory=state.memory,
        nerve=state.nerve
    )

from app.interfaces.api.openai_router import router as openai_router, get_run_debate_use_case as get_openai_use_case

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
from app.interfaces.mcp_server import mcp
app.mount("/mcp", mcp.sse_app())

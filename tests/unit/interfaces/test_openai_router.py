import pytest
from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import AsyncMock, patch, MagicMock
from app.domain.entities import DebateResult

client = TestClient(app)

@pytest.mark.asyncio
async def test_openai_chat_completions():
    """
    Test the OpenAI-compatible chat completions endpoint.
    It should:
    1. Accept OpenAI-formatted request.
    2. Extract the topic from messages.
    3. Call execute_stream.
    4. Return SSE stream in OpenAI format.
    """
    
    # Mocking the UseCase dependency
    mock_use_case = MagicMock()
    
    # Mock execute_stream to yield chunks
    async def mock_generator(topic, model_name=None):
        yield "Hello"
        yield " World"
        
    mock_use_case.execute_stream.side_effect = mock_generator
    
    # We need to override the dependency in the app
    # Use app.dependency_overrides
    # IMPORTANT: Must import the exact function object used in the router endpoint
    from app.interfaces.api.openai_router import get_run_debate_use_case
    app.dependency_overrides[get_run_debate_use_case] = lambda: mock_use_case
    
    request_data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "user", "content": "Test Topic"}
        ],
        "stream": True
    }
    
    response = client.post("/openai/v1/chat/completions", json=request_data)
    
    # Assert
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/event-stream; charset=utf-8"
    
    content = response.text
    
    # OpenAI Stream Format Check
    # content should contain "data: ..." lines
    assert "data: " in content
    assert "Hello" in content
    assert "World" in content
    
    # Clean up
    app.dependency_overrides = {}

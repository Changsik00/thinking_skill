import pytest
from unittest.mock import AsyncMock, MagicMock
from app.usecases.manage_debates import ListDebatesUseCase, GetDebateUseCase
from app.domain.entities import DebateResult

@pytest.fixture
def mock_memory_vault():
    return AsyncMock()

@pytest.fixture
def mock_results():
    return [
        DebateResult(topic="T1", content="C1", model="M1", created_at="2024-01-01"),
        DebateResult(topic="T2", content="C2", model="M2", created_at="2024-01-02")
    ]

@pytest.fixture
def mock_result():
    return DebateResult(topic="T1", content="C1", model="M1", created_at="2024-01-01")

@pytest.mark.asyncio
async def test_list_debates_use_case(mock_memory_vault, mock_results):
    # Setup
    mock_memory_vault.list_debates = MagicMock(return_value=mock_results)
    use_case = ListDebatesUseCase(mock_memory_vault)

    # Execute
    results = await use_case.execute(limit=5)

    # Verify
    mock_memory_vault.list_debates.assert_called_once_with(limit=5)
    assert results == mock_results
    assert len(results) == 2

@pytest.mark.asyncio
async def test_get_debate_use_case_found(mock_memory_vault, mock_result):
    # Setup
    mock_memory_vault.get_debate = MagicMock(return_value=mock_result)
    use_case = GetDebateUseCase(mock_memory_vault)

    # Execute
    result = await use_case.execute(topic="T1")

    # Verify
    mock_memory_vault.get_debate.assert_called_once_with(topic="T1")
    assert result == mock_result
    assert result.topic == "T1"

@pytest.mark.asyncio
async def test_get_debate_use_case_not_found(mock_memory_vault):
    # Setup
    mock_memory_vault.get_debate = MagicMock(return_value=None)
    use_case = GetDebateUseCase(mock_memory_vault)

    # Execute
    result = await use_case.execute(topic="Unknown")

    # Verify
    mock_memory_vault.get_debate.assert_called_once_with(topic="Unknown")
    assert result is None

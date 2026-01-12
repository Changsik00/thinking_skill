from unittest.mock import MagicMock, patch

import pytest
import requests

from app.domain.entities import DebateResult
from app.infrastructure.automation.n8n_adapter import N8nAdapter


@pytest.fixture
def mock_env(monkeypatch):
    # Patch load_dotenv to prevent reading from local .env
    with patch("app.infrastructure.automation.n8n_adapter.load_dotenv"):
        monkeypatch.setenv("N8N_WEBHOOK_URL", "http://mock-n8n.local/webhook")
        yield


def test_trigger_success(mock_env):
    """Verify that trigger sends correct payload and returns success message."""
    adapter = N8nAdapter()
    result = DebateResult(topic="Test Topic", content="Test Summary", model="Test Model")

    with patch("requests.post") as mock_post:
        # Configure mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        # Action
        status = adapter.trigger(result, target="slack")

        # Assertions
        assert "successfully" in status
        assert "slack" in status

        # Verify call args
        mock_post.assert_called_once()
        args, kwargs = mock_post.call_args

        assert args[0] == "http://mock-n8n.local/webhook"
        json_body = kwargs["json"]
        assert json_body["topic"] == "Test Topic"
        assert json_body["summary"] == "Test Summary"
        assert json_body["target"] == "slack"
        assert json_body["source"] == "Thingking Brain"


def test_trigger_failure(mock_env):
    """Verify that trigger handles HTTP errors gracefully."""
    adapter = N8nAdapter()
    result = DebateResult(topic="Fail", content="Fail")

    with patch("requests.post") as mock_post:
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_post.return_value = mock_response

        status = adapter.trigger(result, target="email")

        assert "failed" in status
        assert "500" in status


def test_trigger_exception(mock_env):
    """Verify that trigger handles exceptions (e.g. timeout)."""
    adapter = N8nAdapter()
    result = DebateResult(topic="Error", content="Error")

    with patch(
        "requests.post",
        side_effect=requests.exceptions.ConnectionError("Network Error"),
    ):
        status = adapter.trigger(result)
        assert "Failed to trigger" in status
        assert "Network Error" in status


def test_no_env_var(monkeypatch):
    """Verify that trigger returns warning if ENV not set."""
    # Ensure env is empty just in case
    monkeypatch.delenv("N8N_WEBHOOK_URL", raising=False)

    # Init with explicit None(and env is empty)
    # We also patch load_dotenv here to ensure it doesn't reload .env
    with patch("app.infrastructure.automation.n8n_adapter.load_dotenv"):
        adapter = N8nAdapter(webhook_url=None)

        result = DebateResult(topic="NoEnv", content="NoEnv")
        status = adapter.trigger(result)

        assert "not set" in status

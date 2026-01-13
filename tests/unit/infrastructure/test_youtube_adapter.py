# tests/unit/infrastructure/test_youtube_adapter.py
from unittest.mock import patch

import pytest

from app.infrastructure.external.youtube_adapter import YoutubeAdapter


@pytest.fixture
def adapter():
    return YoutubeAdapter()


def test_get_video_id_valid_formats(adapter):
    """Should correctly extract video ID from various URL formats"""
    # Standard
    assert adapter.get_video_id("https://www.youtube.com/watch?v=dQw4w9WgXcQ") == "dQw4w9WgXcQ"
    # Shortened
    assert adapter.get_video_id("https://youtu.be/dQw4w9WgXcQ") == "dQw4w9WgXcQ"
    # Embed
    assert adapter.get_video_id("https://www.youtube.com/embed/dQw4w9WgXcQ") == "dQw4w9WgXcQ"
    # With extra params
    assert adapter.get_video_id("https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=1s") == "dQw4w9WgXcQ"


def test_get_video_id_invalid(adapter):
    """Should raise ValueError for invalid URLs"""
    with pytest.raises(ValueError):
        adapter.get_video_id("https://google.com")

    with pytest.raises(ValueError):
        adapter.get_video_id("not_a_url")


@patch("app.infrastructure.external.youtube_adapter.YouTubeTranscriptApi")
def test_get_transcript_success(mock_api, adapter):
    """Should fetch and format transcript"""
    # Mock return value of get_transcript
    mock_transcript = [
        {"text": "Hello", "start": 0.0, "duration": 1.0},
        {"text": "World", "start": 1.0, "duration": 1.0},
    ]
    mock_api.get_transcript.return_value = mock_transcript

    # TextFormatter is already used inside adapter, let's just check the string result
    # The default TextFormatter just joins text with newlines
    result = adapter.get_transcript("https://youtu.be/TESTVIDEOID")

    assert "Hello" in result
    assert "World" in result
    mock_api.get_transcript.assert_called_with("TESTVIDEOID", languages=["ko", "en"])


@patch("app.infrastructure.external.youtube_adapter.YouTubeTranscriptApi")
def test_get_transcript_failure(mock_api, adapter):
    """Should handle errors gracefully"""
    mock_api.get_transcript.side_effect = Exception("Video unavailable")

    result = adapter.get_transcript("https://youtu.be/FAILVIDEOID")
    assert "Failed to fetch transcript" in result
    assert "Video unavailable" in result

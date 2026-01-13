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
    """Should fetch and format transcript using list_transcripts"""
    # Mock the chain: list_transcripts -> find_transcript -> fetch
    mock_transcript_list = mock_api.list_transcripts.return_value
    mock_transcript_obj = mock_transcript_list.find_transcript.return_value

    mock_transcript_data = [
        {"text": "Hello", "start": 0.0, "duration": 1.0},
        {"text": "World", "start": 1.0, "duration": 1.0},
    ]
    mock_transcript_obj.fetch.return_value = mock_transcript_data

    # Ensure hasattr checks pass (MagicMock usually has everything, but being explicit helps understanding)
    # The code checks hasattr(YouTubeTranscriptApi, 'list_transcripts'), which patch handles.

    result = adapter.get_transcript("https://youtu.be/TESTVIDEOID")

    assert "Hello" in result
    assert "World" in result

    # Verify the calls
    # Since we check hasattr, we can't easily assert on that, but we can verify list_transcripts call
    mock_api.list_transcripts.assert_called_with("TESTVIDEOID")
    mock_transcript_list.find_transcript.assert_called_with(["ko", "en"])
    mock_transcript_obj.fetch.assert_called_once()


@patch("app.infrastructure.external.youtube_adapter.YouTubeTranscriptApi")
def test_get_transcript_failure(mock_api, adapter):
    """Should handle errors gracefully"""
    # Simulate list_transcripts failing
    mock_api.list_transcripts.side_effect = Exception("Video unavailable")

    # Also ensure fallback doesn't succeed randomly (though patch usually replaces the whole class)
    # The code checks hasattr. MagicMock will have 'list', so the code might try calling .list()
    # Let's verify it handles exception from the first call and returns error
    # OR if it falls back.
    # Actually, in the code:
    # try:
    #    if hasattr(..., list_transcripts): call it
    # except:
    #    fallback...

    # If list_transcripts raises an Exception (not AttributeError), the outer try-catch catches it.

    result = adapter.get_transcript("https://youtu.be/FAILVIDEOID")
    assert "Failed to fetch transcript" in result
    assert "Video unavailable" in result

# app/infrastructure/external/youtube_adapter.py
import re

from youtube_transcript_api import YouTubeTranscriptApi


class YoutubeAdapter:
    def __init__(self):
        pass

    def get_video_id(self, url: str) -> str:
        """
        Extracts video ID from various YouTube URL formats.
        Supports:
        - https://www.youtube.com/watch?v=VIDEO_ID
        - https://youtu.be/VIDEO_ID
        - https://www.youtube.com/embed/VIDEO_ID
        """
        # Regex for common YouTube URL patterns
        regex = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})"  # noqa: E501
        match = re.search(regex, url)
        if not match:
            raise ValueError(f"Invalid YouTube URL: {url}")
        return match.group(1)

    def get_transcript(self, url: str) -> str:
        """
        Fetches transcript for a given YouTube URL.
        Returns combined text provided by the formatter.
        """
        try:
            video_id = self.get_video_id(url)
            # Fetch transcript (tries to get manual subs first, then auto-generated)
            # Default to English or Korean, but falls back to any available
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["ko", "en"])

            # Format to plain text
            # Manually join text to avoid dependency issues with TextFormatter expecting objects vs dicts
            return "\n".join([item["text"] for item in transcript])
        except Exception as e:
            return f"Failed to fetch transcript: {str(e)}"

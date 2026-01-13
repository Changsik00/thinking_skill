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
            
            # Try standard static API first
            try:
                if hasattr(YouTubeTranscriptApi, 'list_transcripts'):
                    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
                elif hasattr(YouTubeTranscriptApi, 'list'):
                     # Try static list if possible (unlikely given previous error, but safe check)
                     # If this fails with missing arg, the except block below might catch it? 
                     # Actually, calling it and failing is better handled by try-except.
                     transcript_list = YouTubeTranscriptApi.list(video_id)
                else:
                    raise AttributeError("No list method found")
            except (AttributeError, TypeError):
                # Fallback: The installed version requires instantiation (e.g. YouTubeTranscriptApi().list(...))
                api = YouTubeTranscriptApi()
                if hasattr(api, 'list_transcripts'):
                    transcript_list = api.list_transcripts(video_id)
                elif hasattr(api, 'list'):
                    transcript_list = api.list(video_id)
                else:
                    raise
            
            # Try to find Korean or English transcript (manual or auto)
            # find_transcript searches for the first available language in the list
            try:
                transcript = transcript_list.find_transcript(['ko', 'en'])
            except Exception:
                # If specific languages not found, try to get any available transcript
                # This might happen if video only has 'es' or 'fr' etc.
                # iterate and pick first
                transcript = next(iter(transcript_list))

            # Fetch the actual data
            transcript_data = transcript.fetch()

            # Format to plain text
            lines = []
            for item in transcript_data:
                if isinstance(item, dict):
                    lines.append(item["text"])
                else:
                    # Assume object with .text attribute
                    lines.append(item.text)
            return "\n".join(lines)
        except Exception as e:
            return f"Failed to fetch transcript: {str(e)}"

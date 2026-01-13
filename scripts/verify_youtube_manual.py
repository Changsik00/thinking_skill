import asyncio

from app.infrastructure.external.youtube_adapter import YoutubeAdapter


async def main():
    adapter = YoutubeAdapter()
    # A standard persistent video (Rick Astley - Never Gonna Give You Up) to ensure it works
    # Or a TED talk: https://www.youtube.com/watch?v=zIwLWfaAg-8 (The first 20 hours)
    url = "https://www.youtube.com/watch?v=zIwLWfaAg-8"

    print(f"Fetching transcript for: {url}")
    try:
        transcript = adapter.get_transcript(url)
        print("\n--- Success! Transcript Preview (First 500 chars) ---")
        print(transcript[:500])
        print("...\n(Total length: ", len(transcript), " characters)")
        print("-----------------------------------------------------")
        print("If you see text above, the AI will see it too!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())

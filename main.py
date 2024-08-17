from youtube_transcript_api import YouTubeTranscriptApi
import argparse

def get_transcript(video_url):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_url)
        text = ' '.join([entry['text'] for entry in transcript])
        return text
    except Exception as e:
        print(f"Error: {e}")
        return None

def save_transcript_to_file(transcript, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(transcript)
        print(f"Transcription saved to {output_file}")
    except Exception as e:
        print(f"Error saving transcription to file: {e}")

def main():
    parser = argparse.ArgumentParser(description="YouTube Video Transcription")
    parser.add_argument("video_url", help="YouTube video URL")
    parser.add_argument("--output_file", help="Output file to save the transcription (default: transcript.txt)", default="transcript.txt")
    args = parser.parse_args()

    video_url = args.video_url
    output_file = args.output_file

    transcript = get_transcript(video_url)

    if transcript:
        print("Transcript:")
        print(transcript)
        save_transcript_to_file(transcript, output_file)
    else:
        print("Transcription failed.")

if __name__ == "__main__":
    main()

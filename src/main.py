import conversions


def main() -> None:
    """
    Main function that sets the YouTube video link and calls the download function.
    """
    # Set the YouTube video link to download.
    yt_link: str = "https://www.youtube.com/watch?v=5NPoVzswK38"

    # Download the video from the provided YouTube link.
    video_path: str = conversions.downloadYtVideo(url=yt_link)
    video_path: str = video_path.replace('.f251', "")

    # Convert the .webm video to a .wav audio file.
    wav_path: str = conversions.convertWebmToWav(video_path)


if __name__ == "__main__":
    """
    Entry point of the script. Executes the main function.
    """
    # Enter the main function.
    main()

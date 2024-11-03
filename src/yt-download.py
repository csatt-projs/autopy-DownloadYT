from pytube import YouTube


def download_youtube_video(vid_link: str, output_path: str):

    yt = YouTube(url=vid_link)

    yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first().download(output_path)

    return


if __name__ == "__main__":

    yt_link: str = "https://www.youtube.com/watch?v=5NPoVzswK38"

    out_path: str = "C:\\GitHub-@csatt\\autopy-DownloadYT\\output"

    download_youtube_video(yt_link, out_path)

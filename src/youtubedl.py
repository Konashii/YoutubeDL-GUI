import yt_dlp


# This is to hide the annoying output on the terminal
class LogOutput:
    def error(msg) -> None:
        return
    def warning(msg) -> None:
        return
    def debug(msg) -> None:
        return


def video_info(url: str) -> dict:
    data = {}
    
    ydl_opts = {
        "extract_info": True,
        "quiet": True,
        "logger": LogOutput,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)

        data["title"] = info_dict.get("title", None)
        data["duration"] = info_dict.get("duration", None)
        data["filesize"] = info_dict.get("filesize_approx", None)
    
    return data
    

def download_video(url: str, dst: str, audio: bool = False) -> None:
    
    outtmpl = f"{dst}/%(title)s.%(ext)s"
    
    ydl_opts = {
        "outtmpl": outtmpl,
        "format": "bestvideo+bestaudio/best"
    }
    
    if audio:
        print("AUDIO IS TRUE IF THIS IS RUN")
        ydl_opts = {
            "outtmpl": outtmpl,
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)

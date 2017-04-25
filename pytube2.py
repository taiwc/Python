from pytube import YouTube

yt = YouTube()
yt.url = "https://www.youtube.com/watch?v=27ob2G3GUCQ"
print("Source:" + yt.filename)
yt.set_filename("Magic1")
print("download" + yt.filename)
print("Format" + str(yt.get_videos()))
print("mp4" + str(yt.filter("mp4")))
video = yt.get("mp4", "360p")
video.download("tem")
print("Download d:\\tem folder, filename Magic1.mp4")

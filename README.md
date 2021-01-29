Hi!

These are simple python programs (tried my best to make it as straightforward as could be) that you can use to easily convert youtube videos to thei mp3 or mp4 equivalents
# This is for educational and exposure purposes only

Pakages you should install for these programmes to work
# pytube, moviepy and shutil

# -Sidenote:
you may see the 'itag' keyword being used to download the video in Yt_to_mp4.py- basically the 'itag' is an integer value that is used to denote a certain quality of resolution available of the video like: 240p, 360p, 480p, 720p ... and so on, now the 'itag' values for the video quality and fps are as-

# these can be seen by executing the line: 
   
  print(yt.streams.filter(only_video=True))

 <Stream: itag="137" mime_type="video/mp4" res="1080p" fps="30fps" vcodec="avc1.640028" progressive="False" type="video">,
 <Stream: itag="248" mime_type="video/webm" res="1080p" fps="30fps" vcodec="vp9" progressive="False" type="video">,
 <Stream: itag="136" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.4d401f" progressive="False" type="video">,
 <Stream: itag="247" mime_type="video/webm" res="720p" fps="30fps" vcodec="vp9" progressive="False" type="video">,
 <Stream: itag="135" mime_type="video/mp4" res="480p" fps="30fps" vcodec="avc1.4d401e" progressive="False" type="video">,
 <Stream: itag="244" mime_type="video/webm" res="480p" fps="30fps" vcodec="vp9" progressive="False" type="video">,
 <Stream: itag="134" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.4d401e" progressive="False" type="video">,
 <Stream: itag="243" mime_type="video/webm" res="360p" fps="30fps" vcodec="vp9" progressive="False" type="video">,

Now according to your needs you may enter the itag value that matches the resolution you want to download

Practice discretion and,
Enjoy!

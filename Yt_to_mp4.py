from pytube import YouTube

#ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)

#Getting the highest resolution possible
print(yt.streams.filter(progressive = True))
tag = input('Please select 18 for 360p and 22 for 720p video quality:  ')
ys = yt.streams.get_by_itag(int(tag))

#Starting download
print("Downloading...")
ys.download('C:/Users/your_name/videos folder')
print("Download completed!!")

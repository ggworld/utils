from moviepy.editor import *
clip = VideoFileClip("/Users/geva/Downloads/VID_20211118_224414.mp4") 
clip = clip.subclip(1, 33) 

#geting the united audio file and addig it to clip 

#if the video was taken in portrait :
w, h = clip.size
clip = clip.resize((w/3 , h ))
videoclip = clip



#Saving the new combine file 
videoclip.write_videofile("/Users/geva/Downloads/haleluya.mp4", temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")

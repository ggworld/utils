#good source and example for this package : https://www.programcreek.com/python/example/105718/moviepy.editor.VideoFileClip

from moviepy.editor import *
my_list ={}

#looping on all video files named 1-7 
for i in range(1,8):
    my_list[i]=VideoFileClip(f"/Users/geva/Documents/private/tmp/WhatsApp{i}.mp4")


new_clip = concatenate_videoclips(list(my_list.values()))

#Saving the new combine file 
new_clip.write_videofile("/Users/geva/Downloads/test3.mp4", temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")

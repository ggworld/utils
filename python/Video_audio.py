from moviepy.editor import *


audioclip = AudioFileClip("/Users/geva/Downloads/shorter_audio.mp3")
audioclip1 = AudioFileClip("/Users/geva/Downloads/shorter_audio1.mp3")
#concatinate multiple audio files 
new_c = concatenate_audioclips([audioclip,audioclip1])
new_c.write_audiofile('/Users/geva/Downloads/twice_shorter_audio.mp3')

#Getting Video file and slicing it 
clip = VideoFileClip("/Users/geva/Downloads/baba.mp4") 
clip = clip.subclip(7, 63) 

#geting the united audio file and addig it to clip 
audioclip = AudioFileClip("/Users/geva/Downloads/twice_shorter_audio.mp3")
videoclip = clip.set_audio(audioclip)

#Saving the new combine file 
videoclip.write_videofile("/Users/geva/Downloads/test3.mp4", temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")


import moviepy.editor as mp

def clipmaking():
    video_path = "videotest.mp4"
    audio_path = "test.mp3"

    video = mp.VideoFileClip(video_path)
    audio = mp.AudioFileClip(audio_path)

    final_video = video.set_audio(audio)
    final_video = final_video.set_duration(audio.duration)

    output_filename = "output_video.mp4"
    final_video.write_videofile(output_filename, codec='libx264')



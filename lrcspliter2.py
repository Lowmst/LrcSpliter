import os

original_lyrics_file_list = os.listdir("original")
chinese_lyrics_file_list = os.listdir("chinese")

for original_lyrics_file in original_lyrics_file_list:
    for chinese_lyrics_file in chinese_lyrics_file_list:
        if chinese_lyrics_file == original_lyrics_file:
            lyrics_file_list=[original_lyrics_file,chinese_lyrics_file]
        else:
            lyrics_file_list=[original_lyrics_file]
        
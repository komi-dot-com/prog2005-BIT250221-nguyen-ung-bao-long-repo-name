import os

def get_filename_from_path(path):
  return os.path.basename(path)

def get_song_name_from_path(path):
  filename = os.path.basename(path)
  return os.path.splitext(filename)[0]

path = "d:\\music\\muabui.mp3"
print(f"Đường dẫn đầy đủ: {path}")
print(f"Tên tệp: {get_filename_from_path(path)}")
print(f"Tên bài hát: {get_song_name_from_path(path)}")

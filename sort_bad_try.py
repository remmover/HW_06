import os
import sys
import shutil
from pathlib import Path

images_extension = ('.jpeg', '.png', '.jpg', '.svg')
video_extension = ('.avi', '.mp4', '.mov', '.mkv')
documents_extension = ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx')
audio_extension = ('.mp3', '.ogg', '.wav', '.amr')
archives_extension = ('.zip', '.gz', '.tar')
ignored_folders = ("archives", "video", "audio", "documents", "images")
ua = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ -;,()[]{}\'" <> |!@  # $%^&*~`+='
eng = "abvhgdeeezyiijklmnoprstufhccss'yaABVHGDEEEZYIIJKLMNOPRSTUFHCCSS'YA________________________________"


def normalize(name):
    TRANS = str.maketrans(ua, eng)
    return str(name).translate(TRANS)


def is_dir_exists(name):
    if not name.exists():
        return name.mkdir()


path = Path(sys.argv[1])

folders_to_del = []

for item in path.glob('**'):
    folders_to_del.append(item)
for item in folders_to_del[::-1]:
    try:
        item.rmdir()
    except Exception as e:
        print(e)

images_path = path / 'images'


documents_path = path / 'documents'


audio_path = path / 'audio'


video_path = path / 'video'


archives_path = path / 'archives'


unknown_items = path / 'unknown'
is_dir_exists(unknown_items)

for item in path.glob('**\*'):
    try:
        item = os.rename(item, normalize(item))
    except:
        PermissionError

for item in path.glob('**\*'):
    path_item = str(item)
    extension = str(item.suffix.lower())
    directory = os.path.dirname(item)
    # print(directory.split('\\')[-1],item)
    if item.name not in ("archives", "video", "audio", "documents", "images"):
        if extension in images_extension:
            is_dir_exists(images_path)
            file_in_target = os.replace(item, images_path / item.name)

        elif extension in video_extension:
            is_dir_exists(video_path)
            file_in_target = os.replace(
                item, video_path / item.name)

        elif extension in documents_extension:
            is_dir_exists(documents_path)
            file_in_target = os.replace(
                item, documents_path / item.name)
            
        elif extension in audio_extension:
            is_dir_exists(audio_path)
            file_in_target = os.replace(item, audio_path / item.name)

        elif extension in archives_extension:
            is_dir_exists(archives_path)
            new_archive = archives_path / item.name.split('.')[-2]
            is_dir_exists(new_archive)
            shutil.unpack_archive(path_item, new_archive)
            os.remove(item)
        # else:
        #     file_in_target = os.replace(item, unknown_items / item.name)
    else:
        continue

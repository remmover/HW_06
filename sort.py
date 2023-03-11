import sys
import shutil
from pathlib import Path
import os


CATEGORIES = {'audio': ['.mp3', '.ogg', '.wav', '.amr'],
              'image': ['.jpeg', '.png', '.jpg', '.svg'],
              'video': ['.avi', '.mp4', '.mov', '.mkv'],
              'document': ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
              'archive': ['.zip', '.gz', '.tar']}

ua = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ -;,()[]{}\'" <> |!@  # $%^&*~`+='
eng = "abvhgdeeezyiijklmnoprstufhccss'yaABVHGDEEEZYIIJKLMNOPRSTUFHCCSS'YA________________________________"


def normalize(name):
    TRANS = str.maketrans(ua, eng)
    return str(name).translate(TRANS)


def move_file(file: Path, root_dir: Path, category: str):

    if category == 'unknown':
        return file.replace(root_dir / normalize(file.name))

    target_folder = root_dir / category

    if not target_folder.exists():
        target_folder.mkdir()

    if category == 'archive':

        archive_folder = target_folder / file.name
        if not archive_folder.exists():
            archive_folder.mkdir()
            normalize(file)
            shutil.unpack_archive(
            file, archive_folder)
            os.remove(file)
            return 'archive is unarchiver'

    return file.replace(target_folder / normalize(file.name))


def get_categories(file):
    extension = file.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if extension in exts:
            return cat
    return 'unknown'


def sort_dir(root_dir: Path, current_dir: Path):
    for item in [i for i in current_dir.glob('*') if i.name not in CATEGORIES.keys()]:
        if not item.is_dir():
            category = get_categories(item)
            new_path = move_file(item, root_dir, category)
            print(new_path)
        else:
            sort_dir(root_dir, item)
            item.rmdir()


def main():
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return f"No path to folder. Take as parameter"

    if not path.exists():
        return f"Sorry, {path} not exists"

    sort_dir(path, path)

    return "All ok"


if __name__ == '__main__':
    print(main())

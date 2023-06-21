# File Sorter

This script is designed to sort files in a specified directory into different categories based on their file extensions. The categories include audio, image, video, document, and archive files.

## Prerequisites

- Python 3.x
- Required Python libraries: `sys`, `shutil`, `pathlib`, `os`

## Usage

1. Clone the repository or download the script file `file_sorter.py` to your local machine.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the following command to execute the script:

   ```bash
   python file_sorter.py <path_to_folder>
   ```

   Replace `<path_to_folder>` with the actual path to the folder you want to sort.

   **Note:** Make sure you have the necessary permissions to read and modify the files in the specified folder.

4. The script will scan the folder and its subdirectories, identify the file categories based on their extensions, and move them to corresponding category folders.

## File Categories

The script categorizes files into the following categories:

- **Audio**: Files with extensions `.mp3`, `.ogg`, `.wav`, and `.amr`.
- **Image**: Files with extensions `.jpeg`, `.png`, `.jpg`, and `.svg`.
- **Video**: Files with extensions `.avi`, `.mp4`, `.mov`, and `.mkv`.
- **Document**: Files with extensions `.doc`, `.docx`, `.txt`, `.pdf`, `.xlsx`, and `.pptx`.
- **Archive**: Files with extensions `.zip`, `.gz`, and `.tar`.

Files with extensions not matching any of the above categories will be categorized as "unknown".

## Notes

- If the category of a file is "unknown", the script will attempt to normalize the file name and move it to the root directory.
- For files categorized as "archive", the script will create a corresponding folder with the same name as the archive file and unpack the contents of the archive into that folder. The original archive file will be deleted.
- Directories within the specified folder will be recursively sorted as well. Empty directories will be removed after the sorting process.

## Disclaimer

Use this script at your own risk. Make sure to backup your files before running the script, especially when working with important data.

## License

This script is released under the [MIT License](LICENSE).

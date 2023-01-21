import zipfile as zf
import pathlib as pl

def make_archive(filepaths, destination_folder):
    dest_folder = pl.Path(destination_folder, "compressed2.zip")
    with zf.ZipFile(dest_folder, "w") as file:
        for filepath in filepaths:
            filepath = pl.Path(filepath)
            file.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    make_archive(filepaths=["practice2.py", "practice3.py", "sides.txt"], destination_folder="dest_directory")
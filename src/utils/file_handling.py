import os
from typing import List
from fastapi import UploadFile

UPLOAD_DIR = "static/ProfilePhoto/"


def save_uploaded_file(file: UploadFile) -> List[str]:
    if not os.path.exists(UPLOAD_DIR):
        print("Entro")
        os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return [file_path, file.filename]

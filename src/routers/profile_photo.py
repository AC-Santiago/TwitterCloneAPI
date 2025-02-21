from typing import Annotated
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlmodel import Session
from starlette.responses import FileResponse
from crud.user import get_user_by_email
from models.models import ProfilePhotos
from crud.profile_photo import create_image, get_image_by_user_id

from database.connection import get_session
from utils.auth import decode_token
from utils.file_handling import save_uploaded_file

router = APIRouter()


@router.post(
    "/user/me/profile_photo",
    tags=["profile_photo"],
    response_model=ProfilePhotos,
)
def upload_image(
    user: Annotated[dict, Depends(decode_token)],
    file: UploadFile = File(...),
    db: Session = Depends(get_session),
):
    try:
        filepath, filename = save_uploaded_file(file)
        user = get_user_by_email(db, user["email"])
        user_id = user.id
        db_image = create_image(
            db, file_name=filename, file_path=filepath, user_id=user_id
        )
        return db_image
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/user/me/profile_photo",
    tags=["profile_photo"],
    response_model=ProfilePhotos,
)
def read_image_by_user_id(
    user: Annotated[dict, Depends(decode_token)],
    db: Session = Depends(get_session),
):
    user_id = get_user_by_email(db, user["email"]).id
    db_image = get_image_by_user_id(db, user_id=user_id)
    if db_image is None:
        raise HTTPException(
            status_code=404, detail="Image not found for this user"
        )
    return FileResponse(
        path=db_image.file_path,
    )

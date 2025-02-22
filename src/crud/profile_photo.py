from sqlmodel import Session, select
from models.models import ProfilePhotos


def create_image(db: Session, file_name: str, file_path: str, user_id: int):
    db_image = ProfilePhotos(
        file_name=file_name, file_path=file_path, user_id=user_id
    )
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image


def get_image_by_user_id(db: Session, user_id: int):
    return db.exec(
        select(ProfilePhotos).where(ProfilePhotos.user_id == user_id)
    ).first()


def create_or_update_image(db: Session, file_name: str, file_path: str, user_id: int):
    existing_image = get_image_by_user_id(db, user_id)
    if existing_image:
        existing_image.file_name = file_name
        existing_image.file_path = file_path
        db.add(existing_image)
        db.commit()
        db.refresh(existing_image)
        return existing_image
    else:
        return create_image(db, file_name, file_path, user_id)
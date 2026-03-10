from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import User
from schemas import ProfileUpdate

router = APIRouter()


@router.put("/profile/update/{user_id}")
def update_profile(user_id: int, data: ProfileUpdate, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.user_id == user_id).first()

    user.name = data.name
    user.bio = data.bio
    user.phone = data.phone

    db.commit()

    return {"message": "Profile updated"}
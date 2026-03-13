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

@router.get("/profile/{user_id}")
def get_profile(user_id: int, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.user_id == user_id).first()

    if not user:
        return {"message": "User not found"}

    return {
        "user_id": user.user_id,
        "name": user.name,
        "email": user.email,
        "bio": user.bio,
        "phone": user.phone
    }

@router.delete("/profile/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.user_id == user_id).first()

    if not user:
        return {"message": "User not found"}

    db.delete(user)
    db.commit()

    return {"message": "User deleted successfully"}
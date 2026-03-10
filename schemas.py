from pydantic import BaseModel, EmailStr, field_validator


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

    @field_validator("email")
    @classmethod
    def validate_nitp_email(cls, value):
        if not value.endswith("@nitp.ac.in"):
            raise ValueError("Email must belong to @nitp.ac.in domain")
        return value


class LoginSchema(BaseModel):
    email: EmailStr
    password: str


class ProfileUpdate(BaseModel):
    name: str
    bio: str
    phone: str
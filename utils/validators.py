import re
from fastapi import HTTPException


def validate_password(password: str):
    if len(password) < 8:
        raise HTTPException(status_code=400, detail="Password is too short")
    
    if len(password) > 20:
        raise HTTPException(status_code=400, detail="Password is too long")

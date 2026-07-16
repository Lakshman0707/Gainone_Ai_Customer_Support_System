from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer

from app.config import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES
)

# ==========================================
# Password Hashing Configuration
# ==========================================

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# ==========================================
# OAuth2 Scheme
# ==========================================

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

# ==========================================
# Hash Password
# ==========================================

def hash_password(password: str):
    return pwd_context.hash(password)

# ==========================================
# Verify Password
# ==========================================

def verify_password(
    plain_password: str,
    hashed_password: str
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )

# ==========================================
# Create JWT Access Token
# ==========================================

def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update(
        {
            "exp": expire
        }
    )

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt

# ==========================================
# Verify JWT Token
# ==========================================

def verify_token(token: str):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid Token"
            )

        return payload

    except JWTError:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token Expired or Invalid"
        )

# ==========================================
# Get Current Logged-in User
# ==========================================

def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    return verify_token(token)
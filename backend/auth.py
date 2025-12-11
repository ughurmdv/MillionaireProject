from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def _truncate(password: str) -> str:
    if password is None:
        return ""
    return password[:72]


def hash_password(password: str) -> str:
    password = _truncate(password)
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    plain = _truncate(plain)
    return pwd_context.verify(plain, hashed)

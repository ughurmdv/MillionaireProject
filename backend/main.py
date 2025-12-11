from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base
from models import User
from schemas import UserCreate, UserOut, ScoreIn
from auth import hash_password, verify_password
from questions import get_game_questions, get_random_question_by_difficulty


Base.metadata.create_all(bind=engine)


app = FastAPI(title="Millionaire Game API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://millionaireproject-1.onrender.com",
        "http://localhost:8000" 
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Millionaire Game API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already taken")

    new_user = User(
        username=user.username,
        password=hash_password(user.password),
        total_money=0,
    )
    db.add(new_user)
    db.commit()
    return {"message": "Signup successful"}


@app.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    return {"message": "Login successful", "username": db_user.username}


@app.get("/questions")
def questions():
    return get_game_questions()

@app.get("/question_new/{difficulty}")
def question_new(difficulty: str):
    try:
        q = get_random_question_by_difficulty(difficulty)
        return q
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid difficulty")


@app.post("/score")
def submit_score(score: ScoreIn, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == score.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.total_money += score.earned
    db.commit()
    return {"message": "Score updated", "total_money": user.total_money}


@app.get("/leaderboard", response_model=list[UserOut])
def leaderboard(db: Session = Depends(get_db)):
    users = db.query(User).order_by(User.total_money.desc()).limit(20).all()
    return users

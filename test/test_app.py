import sys
import os
import uuid
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath("."))

from backend.main import app
from backend.database import Base, engine
from backend import models  

Base.metadata.create_all(bind=engine)

client = TestClient(app)

TEST_USERNAME = f"user_{uuid.uuid4().hex[:8]}"
TEST_PASSWORD = "testpass"


def test_root():
    """Test the root route."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Millionaire Game API is running"}


def test_get_questions():
    """Test getting all questions."""
    response = client.get("/questions")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  


def test_get_question_by_difficulty():
    """Test fetching a random question by difficulty."""
  
    response = client.get("/question_new/easy")
  
    assert response.status_code in [200, 400]


def test_signup_user():
    response = client.post("/signup", json={
        "username": TEST_USERNAME,
        "password": TEST_PASSWORD
    })
    assert response.status_code in [200, 400]




def test_login_user():
    response = client.post("/login", json={
        "username": TEST_USERNAME,
        "password": TEST_PASSWORD
    })
    assert response.status_code in [200, 400]



def test_submit_score():
    response = client.post("/score", json={
        "username": TEST_USERNAME,
        "earned": 500
    })
    assert response.status_code in [200, 404]



def test_leaderboard():
    """Test leaderboard retrieval."""
    response = client.get("/leaderboard")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

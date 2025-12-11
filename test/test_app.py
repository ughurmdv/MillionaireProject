import sys
import os
from fastapi.testclient import TestClient


sys.path.insert(0, os.path.abspath("."))

from backend.main import app

client = TestClient(app)


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
    """Test user signup."""
    response = client.post("/signup", json={
        "username": "testuser",
        "password": "testpass"
    })

    assert response.status_code in [200, 400]


def test_login_user():
    """Test user login."""
    response = client.post("/login", json={
        "username": "testuser",
        "password": "testpass"
    })
  
    assert response.status_code in [200, 400]


def test_submit_score():
    """Test score submission for an existing user."""
    response = client.post("/score", json={
        "username": "testuser",
        "earned": 500
    })
  
    assert response.status_code in [200, 404]


def test_leaderboard():
    """Test leaderboard retrieval."""
    response = client.get("/leaderboard")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

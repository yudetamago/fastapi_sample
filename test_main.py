from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "title": "Task 1",
        },
        {
            "id": 2,
            "title": "Task 2",
        },
    ]


def test_read_task():
    response = client.get("/tasks/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Task 1",
    }

    response = client.get("/tasks/2")
    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "title": "Task 2",
    }

    response = client.get("/tasks/3")
    assert response.status_code == 200
    assert response.json() == {
        "error": "Task not found",
    }

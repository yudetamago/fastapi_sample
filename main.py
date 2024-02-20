from fastapi import FastAPI
from task import tasks
import uvicorn

app = FastAPI()


@app.get("/tasks")
def read_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return {"error": "Task not found"}


@app.get("/tasks/search/{search_text}")
def search_task(search_text: str):
    result = []
    for task in tasks:
        if search_text.lower() in task["title"].lower():
            result.append(task)
    return result


@app.get("tasks/search2/{search_text}")
def search_task2(search_text: str):
    """use list comprehension"""
    return [task for task in tasks if search_text.lower() in task["title"].lower()]


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1")

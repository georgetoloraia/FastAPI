from typing import Union
from fastapi import FastAPI, status, HTTPException

app = FastAPI()

tasks = [
    {"id": 17, "title": "Task 1", "completed": True },
    {"id": 18, "title": "Buy Milk", "completed": False },
    {"id": 19, "title": "Read book", "completed": False },
    {"id": 20, "title": "Wash the car", "completed": False },
]

@app.get("/")
def read_root():
    return {
        "info": "This is simple todo app for managing your daily tasks",
        "tasks_list": "/tasks"
        }

@app.get("/tasks/")
def read_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def read_task(task_id: int, q = None):
    result = None
    for task in tasks:
        if task["id"] == task_id:
            result = task

    if (result == None):
        raise HTTPException(status_code=404, detail=f"{status.HTTP_404_NOT_FOUND} - Task not found")
    else:
        return result

@app.post("/tasks/")
def create_task(task: dict):
    tasks.append(task)
    return "Reacieved"

@app.put("/tasks/{task_id}")
def update_task(task_id: int, new_task: dict):
    for i, task in enumerate(tasks):
        if (task["id"] == task_id):
            tasks[i] = new_task
            break
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{status.HTTP_404_NOT_FOUND} - Task not found")

    return new_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if(task["id"] == task_id):
            tasks.remove(task)
            break
    else:  
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{status.HTTP_404_NOT_FOUND} - Task not found")
    
    return task_id

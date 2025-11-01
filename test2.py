from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Pydantic 모델
class Task(BaseModel):
    id: int
    title: str
    done: bool = False

class TaskCreate(BaseModel):
    title: str

# 샘플 데이터
tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build REST API", "done": False},
    {"id": 3, "title": "Deploy to production", "done": False}
]

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/tasks", response_model=Task, status_code=201)
async def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "done": False
    }
    tasks.append(new_task)
    return new_task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, done: bool):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task['done'] = done
    return task

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    global tasks
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks = [t for t in tasks if t['id'] != task_id]
    return {"message": "Task deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

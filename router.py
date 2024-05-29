from fastapi import APIRouter
from fastapi import Depends
from schemas import STastAdd
from typing import Annotated
from repository import TaskRepository


router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)

@router.post("")
async def add_task(
    task: Annotated[STastAdd, Depends()],
):
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}




@router.get("")
async def get_tasks():
    tasks = await TaskRepository.get_all()
    return {'tasks': tasks}
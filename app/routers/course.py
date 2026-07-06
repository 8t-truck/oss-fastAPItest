from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class course_data(BaseModel):
  course_name: str
  year: int
  semester: int
  grade: str

courses: list = []

@router.get("/courses")
async def read_all_data()->list:
    return courses

@router.post("/courses")
async def add_list(course_data:course_data)->dict:
    try:
        courses.append(course_data)
        return {
            "course_data":"success"
        }
    except Exception as e:
        raise HTTPException("오류")
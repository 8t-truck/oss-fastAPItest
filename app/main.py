from fastapi import FastAPI
from routers import course

app = FastAPI()

app.include_router(course.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
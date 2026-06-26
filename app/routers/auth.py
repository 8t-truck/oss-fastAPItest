from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv
import httpx
import os

load_dotenv()

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

CLIENT_ID = os.getenv("TOSS_CLIENT_ID")
CLIENT_SECRET = os.getenv("TOSS_CLIENT_SECRET")
TOKEN_URL = "https://openapi.tossinvest.com/oauth2/token"


@router.post("/token")
async def get_access_token():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            TOKEN_URL,
            data={
                "grant_type": "client_credentials",
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
            },
        )
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

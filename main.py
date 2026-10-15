import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from core.browser import pool
from core.resolver import resolve


@asynccontextmanager
async def lifespan(app: FastAPI):
    await pool.start()
    yield
    await pool.stop()


app = FastAPI(title="zLight Bypass API", lifespan=lifespan)


class Req(BaseModel):
    url: str


@app.post("/bypass")
async def bypass(req: Req):
    url = req.url.strip()
    if not url.startswith("http"):
        raise HTTPException(400, "invalid url")

    try:
        result = await resolve(url)
    except Exception as e:
        raise HTTPException(500, f"bypass failed: {e}")

    if not result.get("final_url"):
        raise HTTPException(502, "no final url resolved")

    return {"ok": True, **result}


@app.get("/health")
async def health():
    return {"ok": True}


# static files
os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return FileResponse("static/index.html")

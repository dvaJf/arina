from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()
@app.get("/")
async def serve_index():
    return FileResponse("1.html")
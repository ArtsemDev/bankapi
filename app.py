from fastapi import FastAPI, WebSocket

from api.auth import auth_router
from api import api_router


app = FastAPI()


@app.websocket('/ws')
async def wss(websocket: WebSocket):
    await websocket.accept()
    i = 0
    while True:
        await websocket.send_json({'i': i})


app.include_router(router=auth_router)
app.include_router(router=api_router)

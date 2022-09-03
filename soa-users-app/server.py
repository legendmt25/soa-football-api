from fastapi import FastAPI
import uvicorn

from src.containers import Container
from src.endpoints import router

container = Container()
app = FastAPI()
app.container = container
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, port=container.config.PORT())
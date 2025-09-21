from starlette.middleware.cors import CORSMiddleware

from src.api.containers.routes.containers_route import containers_route
import uvicorn
from fastapi import FastAPI

"""async def  main():
    dock = DockerService()
    result = await dock.get()
    print(result)"""

app =  FastAPI()
app.include_router(containers_route)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)
if __name__ == "__main__":
    uvicorn.run(app)
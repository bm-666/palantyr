from src.api.containers.routes.containers_route import containers_route
import uvicorn
from fastapi import FastAPI

"""async def  main():
    dock = DockerService()
    result = await dock.get()
    print(result)"""

app =  FastAPI()
app.include_router(containers_route)
if __name__ == "__main__":
    uvicorn.run(app)
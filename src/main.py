from src.service.container_service import DockerService
import asyncio


async def  main():
    dock = DockerService()
    result = await dock.get()
    print(result)
if __name__ == "__main__":
    asyncio.run(main())
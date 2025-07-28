from aiodocker import Docker
from src.schemas.container_schema import ContainerSchema

class ContainersRepo:
    def __init__(self, docker: Docker | None = None):
        self.docker = docker or Docker()

    async def find_all(self) -> list[ContainerSchema]:
        containers = await self.docker.containers.list(all=True)
        result = []
        for c in containers:
            data = await c.show()
            for k, v in data.items():
                print(f"{k}: {v}")
            print(data)
            result.append(
                ContainerSchema(
                    container_id=c.id,
                    name=data["Name"].lstrip("/"),
                    status=data["State"]["Status"]
                )
            )
        return result

    async def find_by_id(self, container_id: str) -> ContainerSchema:
        return await self.docker.containers.get(container_id=container_id)


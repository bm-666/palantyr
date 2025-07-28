from aiodocker import Docker
from src.schemas.container_schema import ContainerSchema
from src.repos.container_repo import ContainersRepo

class DockerService:
    def __init__(self, socket: str | None = None):
        self.repo = ContainersRepo()

    async def get(self) -> list[ContainerSchema]:
        return await self.repo.find_all()

    async def get_by_id(self, container_id: str) -> ContainerSchema:
        return await self.repo.find_by_id(container_id)

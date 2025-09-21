from aiodocker import Docker
from src.schemas.container_schema import ContainerSchema
from src.repos.container_repo import ContainersRepo
from src.enums.container_actions import ContainerAction

class DockerService:
    def __init__(self, socket: str | None = None):
        self.repo = ContainersRepo()

    async def get(self) -> list[ContainerSchema]:
        return await self.repo.find_all()

    async def get_by_id(self, container_id: str) -> ContainerSchema:
        return await self.repo.find_by_id(container_id)

    async def perform_action(self, container_id: str, action: ContainerAction):
        await self.repo.execute_action(container_id, action)
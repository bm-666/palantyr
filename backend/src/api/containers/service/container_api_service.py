from src.service.container_service import DockerService
from src.schemas.container_schema import ContainerSchema


class ContainerApiService:
    def __init__(self):
        self.service = DockerService()

    async def containers(self) -> list[ContainerSchema]:
        return await self.service.get()

    async def get_container(self, container_id: str) -> ContainerSchema:
        return await self.service.get_by_id(container_id)

    async def action(self, con):
        pass
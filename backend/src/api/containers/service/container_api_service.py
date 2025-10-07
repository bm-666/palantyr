from src.service.container_service import DockerService
from src.schemas.container_schema import ContainerSchema
from src.enums.container_actions import ContainerAction
from src.enums.container_status_enum import ContainerStatusEnum
class ContainerApiService:
    def __init__(self):
        self.service = DockerService()

    async def containers(self) -> list[ContainerSchema]:
        return await self.service.get()

    async def get_container(self, container_id: str) -> ContainerSchema:
        return await self.service.get_by_id(container_id)

    async def perform_action(self, container_id: str, action: ContainerAction):
        _container = await self.get_container(container_id)

        if action == ContainerAction.START  and _container.status == ContainerStatusEnum.EXITED:
            await self.service.start(container_id)
        elif action ==  ContainerAction.STOP and _container.status == ContainerStatusEnum.RUNNING:
            await self.service.stop(container_id)

        elif action == ContainerAction.PAUSE and _container.status == ContainerStatusEnum.RUNNING:
            await self.service.pause(container_id)

        elif action == ContainerAction.UNPAUSE:
            await self.service.unpause(container_id)


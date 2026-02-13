from aiodocker import Docker

from enums.container_status_enum import ContainerStatusEnum
from src.schemas.container_schema import ContainerSchema
from src.repos.container_repo import ContainersRepo
from src.enums.container_actions import ContainerAction

class DockerService:
    def  __init__(self, socket: str | None = None):
        self.repo = ContainersRepo()

    async def get(self) -> list[ContainerSchema]:
        return await self.repo.find_all()

    async def get_by_id(self, container_id: str) -> ContainerSchema:
        return await self.repo.find_by_id(container_id)

    async def perform_action(self, container_id: str, action: ContainerAction):
        container = await self.get_by_id(container_id)
        print(dir(container))
        match action:
            case ContainerAction.RESTART:
                print("Здесь------------------------>")
                await self.restart(container_id)

            case ContainerAction.START if container.status == ContainerStatusEnum.EXITED:
                #await container.start(container_id)

                await self.start(container_id)
            case ContainerAction.STOP if container.status == ContainerStatusEnum.RUNNING:
                #await container.stop(container_id)
                await self.stop(container_id)
            case ContainerAction.PAUSE if container.status == ContainerStatusEnum.RUNNING:
                #await container.pause(container_id)
                await self.pause(container_id)
            case ContainerAction.START if container.status == ContainerStatusEnum.PAUSED:
                #await container.unpause(container_id)
                await self.unpause(container_id)
            case _:
                raise ValueError(f"Invalid transition {container.status=} → {action=}")

    async def start(self, container_id: str):
        await self.repo.execute_action(container_id, ContainerAction.START)

    async def stop(self, container_id: str):
        await self.repo.execute_action(container_id, ContainerAction.STOP)

    async def restart(self, container_id: str):
        await self.repo.execute_action(container_id, ContainerAction.RESTART)

    async def pause(self, container_id: str):
        await self.repo.execute_action(container_id, ContainerAction.PAUSE)

    async def unpause(self, container_id: str):
        await self.repo.execute_action(container_id, ContainerAction.UNPAUSE)

from src.service.container_service import DockerService


class Manager:
    async def get_container(self):
        docker = DockerService()
        return docker
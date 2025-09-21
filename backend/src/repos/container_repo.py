import asyncio
from aiodocker import Docker

from src.enums.container_actions import ContainerAction
from src.schemas.container_schema import ContainerSchema

class ContainersRepo:
    """
    Repository for interacting with Docker containers via the asynchronous aiodocker client.
    Provides methods for retrieving a list of all containers and fetching a container by its ID.
    """

    def __init__(self, docker: Docker | None = None):
        """
        Initialize the repository.

        Args:
            docker (Docker | None): Optional Docker client instance.
                                   If not provided, a new instance is created.
        """
        self.docker = docker or Docker()

    async def find_all(self) -> list[ContainerSchema]:
        """
        Retrieve a list of all containers with detailed information.

        This method performs an asynchronous request to list all containers,
        and then concurrently fetches detailed information for each container
        and maps the data to ContainerSchema objects.

        Returns:
            list[ContainerSchema]: A list of container schema objects.
        """
        containers = await self.docker.containers.list(all=True)

        async def to_schema(c):
            data = await c.show()
            return self._container_from_dict(c.id, data)

        # Concurrently map all containers to schema objects
        result = await asyncio.gather(*(to_schema(c) for c in containers))
        return result

    async def find_by_id(self, container_id: str) -> ContainerSchema:
        """
        Retrieve information about a container by its ID.

        Args:
            container_id (str): The Docker container ID.

        Returns:
            ContainerSchema: A container schema object with detailed information.
        """
        container = await self.docker.containers.get(container_id=container_id)
        data = await container.show()
        return self._container_from_dict(container_id, data)



    async def execute_action(self, container_id: str, action: ContainerAction):
        container = await self.docker.containers.get(container_id)
        await container.start()
        method = getattr(container, action)
        await method()

    def _container_from_dict(self, container_id: str, data: dict) -> ContainerSchema:
        """
        Convert a dictionary of container information from the Docker API to a ContainerSchema object.

        Args:
            container_id (str): The container ID.
            data (dict): The dictionary of container data retrieved from Docker API.

        Returns:
            ContainerSchema: The container schema object.
        """

        return ContainerSchema(
            container_id=container_id,
            name=data["Name"].lstrip("/"),
            image=data["Config"]["Image"],
            status=data["State"]["Status"],
            started_at=data["State"]["StartedAt"],
            finished_at=data["State"]["FinishedAt"],
            created_at=data["Created"]


        )

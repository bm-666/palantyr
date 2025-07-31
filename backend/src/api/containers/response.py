from src.schemas.container_schema import ContainerSchema
from pydantic import BaseModel


class ContainersResponse(BaseModel):
    containers: list[ContainerSchema]

class ContainerResponse(BaseModel):
    container: ContainerSchema
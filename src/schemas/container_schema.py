from pydantic import BaseModel
from enum import StrEnum

class ContainerStatusEnum(StrEnum):
    CREATED = "created"
    RESTARTING = "restarting"
    RUNNING = "running"
    REMOVING = "removing"
    PAUSED = "paused"
    EXITED = "exited"
    DEAD = "dead"

class BaseContainerSchema(BaseModel):
    container_id: str
    name: str | None = None
    status: ContainerStatusEnum

class ContainerSchema(BaseContainerSchema):
    ...


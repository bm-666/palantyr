from datetime import datetime

from pydantic import BaseModel

from src.enums.container_status_enum import ContainerStatusEnum


class BaseContainerSchema(BaseModel):
    container_id: str
    name: str | None = None
    status: ContainerStatusEnum
    started_at: datetime | None = None
    finished_at: datetime | None = None

class ContainerSchema(BaseContainerSchema):
    ...


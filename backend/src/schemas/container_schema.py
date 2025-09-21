from datetime import datetime

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from src.enums.container_status_enum import ContainerStatusEnum


def format_datetime(dt: datetime) -> str:
    """
    Formats datetime to 'HH:MM:SS DD.MM.YYYY' string.
    """
    return dt.strftime("%H:%M:%S %d.%m.%Y")

class BaseContainerSchema(BaseModel):
    container_id: str
    name: str
    image: str
    status: ContainerStatusEnum
    created_at: datetime | None = None
    started_at: datetime | None = None
    finished_at: datetime | None = None

    model_config = ConfigDict(
        json_encoders = {
            datetime: format_datetime
        },
        alias_generator=to_camel,
        populate_by_name=True
    )

class ContainerSchema(BaseContainerSchema):
    ...


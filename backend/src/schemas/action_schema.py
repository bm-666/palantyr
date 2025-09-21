from src.enums.container_actions import ContainerAction, ContainerActionStatus
from pydantic import BaseModel

class ContainerActionsSchema(BaseModel):
    container_id: str
    action: ContainerAction
    status: ContainerActionStatus
    
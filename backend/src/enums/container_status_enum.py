from enum import StrEnum

class ContainerStatusEnum(StrEnum):
    CREATED = "created"
    RESTARTING = "restarting"
    RUNNING = "running"
    REMOVING = "removing"
    PAUSED = "paused"
    EXITED = "exited"
    DEAD = "dead"
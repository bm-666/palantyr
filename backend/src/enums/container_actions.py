from enum import StrEnum


class ContainerAction(StrEnum):
    START = "start"
    STOP = "stop"
    PAUSE = "pause"
    UNPAUSE = "unpause"
    RESTART = "restart"

class ContainerActionStatus(StrEnum):
    SUCCESS = "success"
    ERROR = "error"
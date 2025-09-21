from fastapi import Path
from typing import Annotated

ContainerID = Annotated[str, Path(..., description="Docker Container ID")]
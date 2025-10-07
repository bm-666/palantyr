from fastapi import APIRouter, Depends
from src.api.dependencies import get_services_manager
from src.service.services_manager import ServicesManager
from src.api.containers.response import ContainersResponse, ContainerResponse
from src.api.containers.params import ContainerID
from src.api.containers.request import ContainerActionRequest

containers_route = APIRouter(
    prefix="/containers",
    tags=["containers"]
)

@containers_route.get(
    "/",
    response_model=ContainersResponse
)
async def containers(
        manager: ServicesManager = Depends(get_services_manager)
):
    containers_service = await manager.get_container_api_service()
    result = await containers_service.containers()

    return {"containers": result}

@containers_route.get(
    "/{container_id}",
    response_model=ContainerResponse,

)
async def get_container_by_id(
    container_id: ContainerID,
    manager: ServicesManager = Depends(get_services_manager),

):
    containers_service = await manager.get_container_api_service()

    result = await containers_service.get_container(container_id)
    return {"container": result}


@containers_route.post("/{container_id}/action")
async def action(
    container_id: ContainerID,
    action: ContainerActionRequest,
    manager: ServicesManager = Depends(get_services_manager),

):
    container_service = await manager.get_container_api_service()
    await container_service.perform_action(container_id, action.action)

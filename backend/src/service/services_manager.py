from src.api.containers.service.container_api_service import ContainerApiService



class ServicesManager:
    async def get_container_api_service(self)-> ContainerApiService:
        container_api_service = ContainerApiService()
        return container_api_service
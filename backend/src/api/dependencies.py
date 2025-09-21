from src.service.services_manager import ServicesManager



async def get_services_manager():
    yield ServicesManager()
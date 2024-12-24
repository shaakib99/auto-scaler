from docker_service.service import DockerContainerService
from prometheus_client import generate_latest, Gauge, Counter, CONTENT_TYPE_LATEST
from fastapi.responses import Response, PlainTextResponse

class MetricsService:
    cpu_usage_in_percentage = Gauge('cpu_usage_in_percentage', 'cpu usage per container', ["container_id"])
    ram_usage_in_percentage = Gauge('ram_usage_in_percentage', 'ram usage per container', ["container_id"])
    storage_usage_in_percentage = Gauge('storage_usage_in_percentage', 'storage usage per container', ["container_id"])
    request_counter = Counter('request_counter', 'Number of requests', ['method', 'endpoint', 'status_code'])
    
    def __init__(self, docker_container_service:DockerContainerService = None):
        self.docker_container_service = docker_container_service or DockerContainerService()
    
    async def caculate_cpu_percentage_from_docker_stats(self, stats):
        if not ("cpu_stats" in stats and "cpu_usage" in stats["cpu_stats"]): 
            return 0
        if not ("cpu_stats" in stats and "system_cpu_usage" in stats["cpu_stats"]): 
            return 0
        if not ("precpu_stats" in stats and "system_cpu_usage" in stats["precpu_stats"]): 
            return 0



        cpu_delta = (
            stats["cpu_stats"]["cpu_usage"]["total_usage"]
            - stats["precpu_stats"]["cpu_usage"]["total_usage"]
        )
        system_delta = (
            stats["cpu_stats"]["system_cpu_usage"]
            - stats["precpu_stats"]["system_cpu_usage"]
        )
        online_cpus = stats["cpu_stats"]["online_cpus"]
        cpu_percentage = max(0, (cpu_delta / system_delta) * online_cpus * 100)
        return cpu_percentage
    
    async def calculate_ram_percentage_from_docker_stats(self, stats):
        memory_usage = stats["usage"]
        memory_limit = stats["limit"]
        memory_percentage = max(0, (memory_usage / memory_limit) * 100)
        return memory_percentage
    
    async def calculate_storage_usage_from_docker_stats(self, stats, unit: str = "GB"):
        io_service_bytes = stats.get("io_service_bytes_recursive", [])

        read_bytes = sum(item["value"] for item in io_service_bytes if item["op"] == "Read")
        write_bytes = sum(item["value"] for item in io_service_bytes if item["op"] == "Write")
        total_storage_usage = read_bytes + write_bytes

        power = 1 # KB
        if unit == "MB":
            power = 2
        elif unit == "GB":
            power = 3
        elif unit == "TB":
            power = 4
        else:
            raise Exception(f"{unit} is not valid")

        total_used_storage = total_storage_usage / (1024 ** power)
        return total_used_storage
    
    async def generate_metrics(self, container_id: str):
        if container_id == 'host':
            return Response(content=generate_latest(), status_code=200)
        docker_stats = await self.docker_container_service.get_stats(container_id)
        if docker_stats is None: 
            return Response(content=None, status_code=404)

        cpu_percentage = await self.caculate_cpu_percentage_from_docker_stats(docker_stats)
        memory_percentage = await self.calculate_ram_percentage_from_docker_stats(docker_stats["memory_stats"])
        total_storage_usage = await self.calculate_storage_usage_from_docker_stats(docker_stats["blkio_stats"], "GB")

        MetricsService.cpu_usage_in_percentage.labels(container_id = container_id).set(cpu_percentage)
        MetricsService.ram_usage_in_percentage.labels(container_id = container_id).set(memory_percentage)
        MetricsService.storage_usage_in_percentage.labels(container_id = container_id).set(total_storage_usage)


        return PlainTextResponse(content=generate_latest(), status_code=200)


from docker_service.service import DockerContainerService
from prometheus_client import generate_latest, Gauge
from fastapi.responses import Response
from docker.errors import NotFound as DockerContainerNotFound
class MetricsService:
    def __init__(self, docker_container_service:DockerContainerService = None):
        self.docker_container_service = docker_container_service or DockerContainerService()
        self.cpu_usage_in_percentage = Gauge('cpu_usage_in_percentage', 'cpu usage per container', ["container_id"])
        self.ram_usage_in_percentage = Gauge('ram_usage_in_percentage', 'ram usage per container', ["container_id"])
        self.storage_usage_in_percentage = Gauge('storage_usage_in_percentage', 'storage usage per container', ["container_id"])
    
    async def caculate_cpu_percentage_from_docker_stats(stats):
        cpu_delta = (
            stats["cpu_usage"]["total_usage"]
            - stats["precpu_stats"]["cpu_usage"]["total_usage"]
        )
        system_delta = (
            stats["system_cpu_usage"]
            - stats["precpu_stats"]["system_cpu_usage"]
        )
        online_cpus = stats["online_cpus"]
        cpu_percentage = max(0, (cpu_delta / system_delta) * online_cpus * 100)
        return cpu_percentage
    
    async def calculate_ram_percentage_from_docker_stats(stats):
        memory_usage = stats["usage"]
        memory_limit = stats["limit"]
        memory_percentage = max(0, (memory_usage / memory_limit) * 100)
        return memory_percentage
    
    async def calculate_storage_usage_from_docker_stats(stats, unit: str = "GB"):
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
        if container_id == "1":
            self.cpu_usage_in_percentage.labels(f"{container_id}").set(50)
            self.ram_usage_in_percentage.labels(f"{container_id}").set(50)
            self.storage_usage_in_percentage.labels(f"{container_id}").set(50)

            return Response(content=generate_latest(), status_code=200)
        docker_stats = await self.docker_container_service.get_stats(container_id)
        if docker_stats is None: 
            return Response(content=generate_latest(), status_code=200)

        cpu_percentage = await self.caculate_cpu_percentage_from_docker_stats(docker_stats["cpu_stats"])
        memory_percentage = await self.calculate_ram_percentage_from_docker_stats(docker_stats["memory_stats"])
        total_storage_usage = await self.calculate_storage_usage_from_docker_stats(docker_stats["blkio_stats"], "GB")

        self.cpu_usage_in_percentage.labels(f"{container_id}").set(cpu_percentage)
        self.ram_usage_in_percentage.labels(f"{container_id}").set(memory_percentage)
        self.storage_usage_in_percentage.labels(f"{container_id}").set(total_storage_usage)

        return Response(content=generate_latest(), status_code=200)


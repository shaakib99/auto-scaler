from enum import Enum

class WorkerStatusEnum(Enum):
    INIT = "init"
    STOPPED = "stopped"
    RUNNING = "running"
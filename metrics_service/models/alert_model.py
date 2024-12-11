from typing import List, Dict, Optional
from pydantic import BaseModel

class AlertAnnotations(BaseModel):
    instance: str

class AlertLabels(BaseModel):
    alertname: str
    container_id: str
    exported_container_id: str
    instance: str
    job: str
    severity: str

class Alert(BaseModel):
    status: str
    labels: AlertLabels
    annotations: AlertAnnotations
    startsAt: str
    endsAt: str
    generatorURL: str
    fingerprint: str

class AlertData(BaseModel):
    receiver: str
    status: str
    alerts: List[Alert]
    groupLabels: Dict[str, str]
    commonLabels: Dict[str, str]
    commonAnnotations: AlertAnnotations
    externalURL: str
    version: str
    groupKey: str
    truncatedAlerts: int

from pydantic import BaseModel
from typing import Optional, Dict

class PrometheusHTTPServiceDiscoveryResponseModel(BaseModel):
    targets: Optional[list] = []
    labels: Optional[Dict[str, str]] = {}
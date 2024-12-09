import pytest
from worker_discovery_service.models import PrometheusHTTPServiceDiscoveryResponseModel    
@pytest.fixture
def mock_worker_discovery_model():
    worker_discovery_model = PrometheusHTTPServiceDiscoveryResponseModel()
    worker_discovery_model.targets = ['host.docker.internal:8000']
    worker_discovery_model.labels = {'__metrics_path__': '/1/metrics', 'container_id': "1"}
    return worker_discovery_model
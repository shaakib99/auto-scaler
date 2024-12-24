# Auto-Scaler

[![Application Unit Test](https://github.com/shaakib99/auto-scaler/actions/workflows/test-app.yml/badge.svg)](https://github.com/shaakib99/auto-scaler/actions/workflows/test-app.yml)

## Introduction
The Auto-Scaler is a lightweight tool designed to monitor Docker container resource usage (CPU, RAM and Storage) and dynamically scale the number of running containers based on predefined thresholds. This ensures optimal performance and resource utilization, making it ideal for applications with fluctuating workloads.

## Features
- **Automatic Scaling**: Automatically starts or stops containers based on CPU and RAM usage.
- **Real-Time Monitoring**: Continuously tracks container resource usage and request using **prometheus** and **Jaeger**.
- **Customizable Thresholds**: Configure CPU and RAM usage limits to trigger scaling actions.
- **Docker Integration**: Fully compatible with Docker environments.

## Requirements
- Python 3.8+
- Docker Engine 20.10+
- `docker` Python SDK
- `MySQL` database
- `SQLAlchemy` ORM
- `Redis`
- `Jaeger`
- `Prometheus`
- `Prometheus-Alertmanager`
- `Postman`

## Running everything
1. Clone the repository:
   ```bash
   git clone https://github.com/shaakib99/auto-scaler.git
   cd auto-scaler
   ```
2. Run docker-compose file:
   ```bash
   docker-compose up -d
   ```

3. Ensure Docker is installed and running on your system.

## Usage
1. Send a POST request using Postman to start a new container:
   - **URL**: `http://localhost:8000/workers`
   - **Body** (JSON):
     ```json
     {
         "ram": 512,
         "cpu": 1
     }
     ```
   This will spin up a Docker container running a simple FastAPI application.

2. Open `http://localhost:9090` and run the `up` command. It should list all servers currently being monitored.

3. Use `request_counter_created` to see all requests and their statuses.

4. To view request traces, navigate to `http://localhost:16686/` (Jaeger UI).

## Pipeline Status
This project uses GitHub Actions for Continuous Integration. The current status of unit tests is displayed below:

[![Application Unit Test](https://github.com/shaakib99/auto-scaler/actions/workflows/test-app.yml/badge.svg)](https://github.com/shaakib99/auto-scaler/actions/workflows/test-app.yml)

## Testing
To run the unit tests for the Auto-Scaler, execute the following command:
```bash
pytest
```
The tests validate core functionality such as:
- Resource usage monitoring
- Container scaling logic
- Docker interactions

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed explanation of your changes.

## Acknowledgements
Special thanks to the open-source community and Docker for providing powerful tools that make projects like this possible.

## Contact
For any questions or feedback, feel free to reach out:
- **GitHub**: [shaakib99](https://github.com/shaakib99)
- **Email**: wsakib87@gmail.com


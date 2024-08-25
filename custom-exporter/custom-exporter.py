# pip install prometheus_client docker

from prometheus_client import start_http_server, Gauge
import docker
import time

# Inicializa el cliente Docker
client = docker.from_env()

# Define la métrica
container_status = Gauge('docker_container_status', 'Estado del contenedor', ['container_name'])

def collect_metrics():
    containers = client.containers.list(all=True)
    for container in containers:
        status = container.status
        container_status.labels(container.name).set(1 if status == 'running' else 0)

if __name__ == '__main__':
    start_http_server(7180)
    while True:
        collect_metrics()
        time.sleep(10)

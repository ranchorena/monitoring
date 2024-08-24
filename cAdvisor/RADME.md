docker build -t custom-cadvisor .

docker run -d --name=cadvisor --volume=/:/rootfs:ro --volume=/var/run/docker.sock:/var/run/docker.sock:ro --volume=/var/lib/docker/:/var/lib/docker:ro --volume=/sys:/sys:ro --volume=/cgroup:/cgroup:ro --publish=7080:8080 --restart=always custom-cadvisor

en varias lineas seria
docker run -d \
  --name=cadvisor \
  --volume=/:/rootfs:ro \
  --volume=/var/run/docker.sock:/var/run/docker.sock:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --volume=/sys:/sys:ro \
  --volume=/cgroup:/cgroup:ro \
  --publish=7080:8080 \
  --restart=always \
  custom-cadvisor
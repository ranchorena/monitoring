# Usa busybox como base para modificar el grupo
FROM busybox:latest as temp

# Añade el grupo docker
RUN addgroup -g 999 docker

# Usa la imagen base original de cAdvisor
FROM gcr.io/cadvisor/cadvisor:latest

# Copia el archivo /etc/group modificado desde la imagen temporal
COPY --from=temp /etc/group /etc/group

# Exponer el puerto y configurar el comando de inicio
EXPOSE 8080
CMD ["/usr/bin/cadvisor"]
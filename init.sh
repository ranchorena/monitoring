#!/bin/sh

# Sustituir la URL del webhook en el archivo de configuración
sed -i "s|${SLACK_WEBHOOK_URL}|${SLACK_WEBHOOK_URL}|g" /etc/alertmanager/alertmanager.yml

# Iniciar Alertmanager
exec /bin/alertmanager

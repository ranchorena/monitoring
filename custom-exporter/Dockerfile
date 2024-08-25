# Utiliza una imagen base ligera de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos y el código de la aplicación al contenedor
COPY requirements.txt .
COPY custom-exporter.py .

# Instala las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 7180
EXPOSE 7180

# Comando para ejecutar el exporter
CMD ["python", "custom-exporter.py"]

# Utiliza una imagen base de Python
FROM python:3.7.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requisitos e instala las dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia todo el código de la aplicación al contenedor
COPY src/ .

# Define el comando para ejecutar la aplicación
CMD ["python", "index.py"]
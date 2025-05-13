#Usa la imagen official de ubuntu version 22.04
FROM ubuntu:22.04
#actualiza al sistema e instala python junto con flask
RUN apt update
RUN apt install python3.10 -y
RUN apt install python3-pip -y
RUN pip3 install flask
#establece el directorio de trabajo
WORKDIR /app
#copiar todos los archivos de esta carpeta a la carpeta app/ en el contenedor
COPY * ./
# Define las variables de entorno por defecto
ENV FLASK_APP=main.py
ENV FLASK_ENV=development
# Expone el puerto que usa la aplicación
EXPOSE 5000
# Comando que se ejecutará al iniciar el contenedor
CMD ["python3.10","main.py"]

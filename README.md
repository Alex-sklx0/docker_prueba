# docker_prueba
# Smashing Pumpkins
Este repositorio contiene un servicio telemático implementado en Python con Flask, contenerizado con Docker para despliegue en producción.
Sitio web sobre The Smashing Pumpkins implementado con Flask y Docker.

## 🚀 Despliegue Rápido

### Requisitos
- Docker instalado
- Git 

### Instalación

```bash
sudo apt update
sudo apt install docker-compose -y

git clone https://github.com/Alex-sklx0/docker_prueba.git
cd docker_prueba
docker build . -t pumpkins-web 
docker run -d -p 80:5000 --name pumpkins_app pumpkins-site
```bash



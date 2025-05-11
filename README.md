# docker_prueba
# Smashing Pumpkins

Sitio web sobre The Smashing Pumpkins implementado con Flask y Docker.

## 🚀 Despliegue Rápido

### Requisitos
- Docker instalado
- Git 

### Instalación
```bash
git clone https://github.com/Alex-sklx0/docker_prueba.git
cd docker_prueba
docker build . -t pumpkins-web 
docker run -d -p 80:5000 --name pumpkins_app pumpkins-site

###Abrir la pagina
En un navegador escribir la ip del host y disfrutar la pagina

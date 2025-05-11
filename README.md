# docker_prueba
# Smashing Pumpkins

[![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)](https://www.docker.com/)
[![Flask](https://img.shields.io/badge/Framework-Flask-green.svg)](https://flask.palletsprojects.com/)

Sitio web fanático de The Smashing Pumpkins implementado con Flask y Docker.

## 🚀 Despliegue Rápido

### Requisitos
- Docker instalado
- Git (opcional)

### Instalación
```bash
git clone https://github.com/tuusuario/smashing-pumpkins-fan-site.git
cd smashing-pumpkins-fan-site
docker build -t pumpkins-site .
docker run -d -p 80:5000 --name pumpkins_app pumpkins-site

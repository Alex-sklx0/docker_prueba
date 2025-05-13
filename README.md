# docker_prueba
# Smashing Pumpkins
Este repositorio contiene un servicio telemático implementado en Python con Flask, contenerizado con Docker para despliegue en producción.
Sitio web sobre The Smashing Pumpkins implementado con Flask y Docker.

## 🚀 Despliegue Rápido

### Requisitos
- Docker instalado
- Git instalado 
```bash
sudo apt update
sudo apt install docker-compose -y
sudo apt install git
```


### Instalación y ejecución
### 1. Clonar el repositorio
```bash
git clone https://github.com/Alex-sklx0/docker_prueba.git
cd docker_prueba
```

### 2. Construir la imagen Docker
```bash
docker build . -t pumpkins-site:web
```
#### 3. Ejecutar el contenedor 
```bash
docker run -d -p 80:5000 pumpkins-site:web 
```
### 4. Verificar el estado
```bash
docker ps
```

# Configuración
Cambios que se pueden hacer:
### Puertos Alternativos
Para usar un puerto diferente al 80:
```bash
docker run -d -p 8080:5000 pumpkins-site:web
```
Para cambiar el puerto que se abre en el contenedor: (dentro del directorio clonado del github)
```bash
nano dockerfile
EXPOSE 5000  # Cambia al nuevo puerto (ej: 8080, 3000, etc.)
```

### Estructura del Proyecto
Tener el cuenta que la estructura del proyecto se ve así:
```
.
├── app/
│   ├── templates/      # Plantillas HTML
│   ├── static/         # Archivos estáticos (CSS, JS)
│   ├── main.py             # Aplicación principal Flask
├── Dockerfile          # Configuración de Docker
└── README.md           # Documentación
```

### Reconstruir después de cambios
Cuando se hagan cambios se debe pausar el contenedore en ejecución:
```bash
docker ps                          # Ver contenedores activos
docker stop pumpkins_prod          # Detener el contenedor
```
Luego se elimina el contenedor:
```bash
docker rm pumpkins_prod            # Eliminar el contenedor
```

```bash
docker build . -t pumpkins-site:web   # Reconstruir imagen
```

Ejecutar de nuevo el contenedor:
```bash
docker run -d -p 80:5000 pumpkins-site:web 
```

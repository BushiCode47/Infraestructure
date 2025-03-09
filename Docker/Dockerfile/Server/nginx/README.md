# Proyecto simple de Nginx con Dockerfile

Este proyecto utiliza un contenedor de Docker con Nginx para servir una página web estática.

## Requisitos

- [Docker](https://www.docker.com/) instalado en tu sistema.

## Instalación y Uso

1. Crea un archivo Dockerfile
Deberás de indicar los pasos de forma correcta. El archivo presentado es un archivo simple para levantar un nginx con una página estática personalizada

2. Crea la estructura de tu página web
Podrás crear tu página web al completo con los archivos necesarios. Destacar que a mayor complejidad tenga la página web, diferentes configuraciones tendrás que hacer en el Dockerfile

3. Construye la imagen de Docker:
   ```sh
   docker build -t mi-nginx:tag .
   ```
La opción -t indica el tag o nombre que deseas que tenga tu imagen seguido de : indicando la versión.
Se le puede añadir un tag diferente en caso de querer subir la imagen a un registry:
    ```
    -t mi_nombre/mi-ningx:v1
    ```

4. Inicia el contenedor:
   ```sh
   docker run -d -p 80:80 --name nginx-servidor <mi-nginx_image>
   ```

4. Abre tu navegador y accede a `http://localhost` para ver tu página web en funcionamiento.

## Personalización

- Para modificar la página web, edita los archivos dentro del directorio `html` y reconstruye la imagen.

## Detener y eliminar el contenedor

```sh
# Detener el contenedor
docker stop nginx-servidor

# Eliminar el contenedor
docker rm nginx-servidor
```

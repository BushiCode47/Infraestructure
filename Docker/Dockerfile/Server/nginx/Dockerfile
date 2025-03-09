#Imagen más ligera de nginx pesando 5MB
FROM nginx:stable-alpine3.20-slim

#Workdir indica el directorio desde el que trabajará, en este caso es el directorio donde nginx muestra las páginas web
WORKDIR /usr/share/nginx/html
#Le indicas que copie los archivos locales en el directorio especificado en el WORKDIR con un .
COPY ./index.html .

#Le indica a Docker que exponga el puerto 80 del contenedor
EXPOSE 80


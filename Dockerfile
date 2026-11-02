FROM nginx:stable-alpine

LABEL org.opencontainers.image.title="Jun Workshop Notes" \
      org.opencontainers.image.description="Codyssey mission 01: reproducible CLI, Docker and Git workshop"

COPY nginx/default.conf /etc/nginx/conf.d/default.conf
COPY site/ /usr/share/nginx/html/

EXPOSE 80

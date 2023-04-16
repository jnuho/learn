

- nginx.conf

```conf
uptream app {
  server flask:5000; # 서버의 컨테이너 명
}

server {
  listen 80;


  location / {
    proxy_pass http://app;
  }
}
```


- Dockerfile

```Dockerfile
FROM nginx:latest


COPY nginx.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]
```


- docker build


```sh
docker build -t nginx:test .
```


- docker-compose.yaml

```yaml
version: '3'
services:
  flask:
    container_name: flask
    image: 'flask:test'
    ports:
      - '5000:5000'
    networks:
      - backend
  nginx:
    container_name: nginx
    image: 'nginx:test'
    ports:
      - '80:80'
    networks:
      - backend
networks:
  backend:
    driver: bridge
```




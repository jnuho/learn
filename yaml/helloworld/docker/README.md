
- Command

```sh
docker login
docker build -t jnuho/server-1 -f build/Dockerfile .
docker push jnuho/server-1
docker pull jnuho/server-1

docker run -d -p 8081:8081 jnuho/server-1
```

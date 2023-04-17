



```sh


sudo apt update
sudo apt install certbot python3-certbot-nginx

sudo certbot certonly --webroot -w /var/www/letsencrypt  -d krms-dev.kaonrms.com

sudo certbot --nginx -d krms-dev.kaonrms.com


# docker-compose.yaml에 letsencrypt 인증서 적용
k31
cd script/nginx
```


- nginx docker-compose up/down 시 포트 충돌
  - 실행 중인 80 포트 프로세스 stop

```sh
sudo netstat -lnp | grep ::80
# Then kill the process 
y the pid returned
sudo kill -15 <PID>
```

1. Namcheap A record 추가
- Host: junho.cloud
- Value: 210.95.66.75

```sh
# check public ip
wget -qO- http://ipecho.net/plain | xargs echo
```

2. certbot 설치

```sh
sudo apt update
sudo apt install certbot python3-certbot-nginx

sudo certbot certonly --standalone -d junho.cloud
```



```conf
  # krms-dev-api
  #server {
  #    listen       8080;

  #   location /api/v1/ {
  #      client_max_body_size 500M;
  #      proxy_pass      http://krms-fe-api:3002;
  #    }
  #    location /auth/v1/ {
  #      client_max_body_size 500M;
  #      proxy_pass      http://krms-fe-auth:3001;
      # error_page 405 = http://krms-fe-auth:3001;
  #    }
  #    location /ws/ {
  #      client_max_body_size 500M;
  #      proxy_pass      http://krms-fe-ws:3003;
  #      proxy_http_version 1.1;
  #      proxy_set_header Upgrade $http_upgrade;
  #      proxy_set_header Connection "Upgrade";
  #    }

  #    location /file/ {
       # proxy_cache_path /data/nginx/cache keys_zone=one:500m loader_files=100;
        #proxy_cache mycache;
  #      alias /download/fw/;
  #    }
  #}
```

https://krms-dev.kaonrms.com/auth/v1/token


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


- 2023-04-14 krms-dev 적용
  - docker-compose down (krms-dev 80포트 서비스를 임시 down)
  - 아래 설정으로 nginx 기동하여 letsencrypt 인증서 발급
  - 발급된 `./data/certbot/conf/live/krms-dev.kaonrms.com/*.pem` 복사
  - krms-nginx 서비스에 적용
    - docker-compose.yaml 설정에서 지정한 volume 디렉토리에 인증서 붙여넣기.
    - nginx.conf에 

- docker-compose.yaml

```yaml
version: '3'

services:
  krms-nginx:
    image: nginx:1.15-alpine
    restart: unless-stopped
    volumes:
      - ./data/nginx:/etc/nginx/conf.d
      - ./data/certbot/conf:/etc/letsencrypt
      - ./data/certbot/www:/var/www/certbot
    ports:
      - "80:80"
      - "443:443"
    command: "/bin/sh -c 'while :; do sleep 6h & wait $${!}; nginx -s reload; done & nginx -g \"daemon off;\"'"
    networks:
      - krms3.1
  krms-nginx-certbot:
    image: certbot/certbot
    restart: unless-stopped
    volumes:
      - ./data/certbot/conf:/etc/letsencrypt
      - ./data/certbot/www:/var/www/certbot
    entrypoint: "/bin/sh -c 'trap exit TERM; while :; do certbot renew; sleep 12h & wait $${!}; done;'"
    networks:
      - krms3.1

networks:
  krms3.1:
    name: krms3.1
    driver: bridge
```

- `init-letsencrypt.sh`

```
#!/bin/bash

if ! [ -x "$(command -v docker-compose)" ]; then
  echo 'Error: docker-compose is not installed.' >&2
  exit 1
fi

domains=(krms-dev.kaonrms.com)
rsa_key_size=4096
data_path="./data/certbot"
email="junho.lee@kaongroup.com" # Adding a valid address is strongly recommended
staging=0 # Set to 1 if you're testing your setup to avoid hitting request limits

if [ -d "$data_path" ]; then
  read -p "Existing data found for $domains. Continue and replace existing certificate? (y/N) " decision
  if [ "$decision" != "Y" ] && [ "$decision" != "y" ]; then
    exit
  fi
fi


if [ ! -e "$data_path/conf/options-ssl-nginx.conf" ] || [ ! -e "$data_path/conf/ssl-dhparams.pem" ]; then
  echo "### Downloading recommended TLS parameters ..."
  mkdir -p "$data_path/conf"
  curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/_internal/tls_configs/options-ssl-nginx.conf > "$data_path/conf/options-ssl-nginx.conf"
  curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot/certbot/ssl-dhparams.pem > "$data_path/conf/ssl-dhparams.pem"
  echo
fi

echo "### Creating dummy certificate for $domains ..."
path="/etc/letsencrypt/live/$domains"
mkdir -p "$data_path/conf/live/$domains"
docker-compose run --rm --entrypoint "\
  openssl req -x509 -nodes -newkey rsa:$rsa_key_size -days 1\
    -keyout '$path/privkey.pem' \
    -out '$path/fullchain.pem' \
    -subj '/CN=localhost'" krms-nginx-certbot
echo


echo "### Starting nginx ..."
docker-compose up --force-recreate -d krms-nginx
echo

echo "### Deleting dummy certificate for $domains ..."
docker-compose run --rm --entrypoint "\
  rm -Rf /etc/letsencrypt/live/$domains && \
  rm -Rf /etc/letsencrypt/archive/$domains && \
  rm -Rf /etc/letsencrypt/renewal/$domains.conf" krms-nginx-certbot
echo


echo "### Requesting Let's Encrypt certificate for $domains ..."
#Join $domains to -d args
domain_args=""
for domain in "${domains[@]}"; do
  domain_args="$domain_args -d $domain"
done

# Select appropriate email arg
case "$email" in
  "") email_arg="--register-unsafely-without-email" ;;
  *) email_arg="--email $email" ;;
esac

# Enable staging mode if needed
if [ $staging != "0" ]; then staging_arg="--staging"; fi

echo "docker-compose run --rm --entrypoint \
  certbot certonly --webroot -w /var/www/certbot \
    $staging_arg \
    $email_arg \
    $domain_args \
    --rsa-key-size $rsa_key_size \
    --agree-tos \
    --force-renewal krms-nginx-certbot"

docker-compose run --rm --entrypoint "\
  certbot certonly --webroot -w /var/www/certbot \
    $staging_arg \
    $email_arg \
    $domain_args \
    --rsa-key-size $rsa_key_size \
    --agree-tos \
    --force-renewal" krms-nginx-certbot
echo

echo "### Reloading nginx ..."
docker-compose exec krms-nginx nginx -s reload

```

- `data/nginx/app.conf`


```conf
server {
    listen 80;
    server_name krms-dev.kaonrms.com;
    server_tokens off;

    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl;
    server_name krms-dev.kaonrms.com;
    server_tokens off;

    ssl_certificate /etc/letsencrypt/live/krms-dev.kaonrms.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/krms-dev.kaonrms.com/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location / {
        proxy_pass  http://krms-dev.kaonrms.com;
        proxy_set_header    Host                $http_host;
        proxy_set_header    X-Real-IP           $remote_addr;
        proxy_set_header    X-Forwarded-For     $proxy_add_x_forwarded_for;
    }
}
```


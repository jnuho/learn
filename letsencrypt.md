



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


I purchased namecheap domain 'junho.cloud' and it seems to have CNAME and TXT record.
I want to link this domain to ubuntu web server.



Saving debug log to /var/log/letsencrypt/letsencrypt.log
Certbot doesn't know how to automatically configure the web server on this system. However, it can still get a certificate for you. Please run "certbot certonly" to do so. You'll need to manually configure your web server to use the resulting certificate.

k

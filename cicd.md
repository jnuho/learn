
- Team City
	- 방법1: Gitlab -> Team City -> DockerHub(private)
	- 방법2: Gitlab -> Team City -> Ubuntu Private Server(setup Docker Registry)

### 방법1

- SetUp
	- Administration > Project 페이지에서 다음 진행 :
	- Create Project
		- Create Project From URL (공통계정 username/pw)
			- `{GitUrl}/{ProjectDir}/{ProjectName}.git`
		- Project name, VCS root, branch
	- Build Configuration
		- Build Steps
			1. set short hash (command line)
			2. docker build
			3. docker push
		- parameters 추가 'GitShortHash=%GitShortHash%'
		- `Edit Project Settings` >  Connections > Add Connections
			- Docker Registry (https://docker.io)
			- 개인 Ubuntu Server를 레지스트리 이용시 추가 필요 X
		- Build Features > docker registry (choose just added docker registry connection)

- On-Premise-Server
	- Public wifi	kaonmedia	172.16.6.77 테스트


### Gitlab (k8s_yaml) 코드작성

```sh
git clone https://devportal.kaonrms.com/konnect/YAML/on-premise/testgohttp.git

cd testgohttp
cat > main.go
package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Hello World!")
	})

	http.ListenAndServe(":8080", nil)
}


go mod init devportal.kaonrms.com/konnect/YAML/on-premise/testgohttp

mkdir build
cat > build/Dockerfile

FROM golang:1.17-alpine as builder

WORKDIR /app

COPY . .

RUN go build -o main .

EXPOSE 8080

CMD ["./main"]
```

### TeamCity

- VCS Root name
https://devportal.kaonrms.com/konnect/cs/krms-mail-sender.git#refs/heads/master

- Fetch URL
https://devportal.kaonrms.com/konnect/cs/krms-mail-sender.git

- Default branch
refs/heads/master

- Branch Specification
refs/heads/*

- Password/Personal Access Token
docker_rep/


- Build steps : CLI

```sh
#!/bin/bash

Hash=%build.vcs.number%
ShortHash=${Hash:0:7}
echo "###teamcity[setParameter name='GitShortHash' value='$ShortHash']"
```


- Build steps : Docker build
	- image:tag
	- 172.16.6.77:5000/my_image:%GitShortHash%
		
- Build steps : Docker push




### 도커 레지스트리 생성


```sh
netstat -anp | grep 5000
docker run -d -p 5000:5000 --restart=always --name registry -v /opt/docker_registry:/var/lib/registry registry:2

```

### 로컬-> 레지스트리

```sh
vim C:\Users\k230303\.docker/daemon.json

{
	"insecure-registries": ["172.16.6.77:5000"]
}

docker tag my_image 172.16.6.77:5000/my_image

docker login 172.16.6.77:5000
docker push 172.16.6.77:5000/my_image
docker pull 172.16.6.77:5000/my_image

docker push jnuho/testgohttp_dockerhub:latest

jnuho/testgohttp_dockerhub:%GitShortHash%
jnuho/testgohttp_dockerhub:latest

## Team City가 아닌 로컬-> 레지스트리 테스트
go mod init devportal.kaonrms.com/konnect/YAML/on-premise/testgohttp
go mod tity
docker build -t my_image -f ./build/Dockerfile .
docker images
	REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
	my_image     latest    0bbcb61acb59   6 seconds ago   320MB


docker tag my_image 172.16.6.77:5000/my_image

winpty docker login http://172.16.6.77:5000
docker push 172.16.6.77:5000/my_image
docker pull 172.16.6.77:5000/my_image
```



- docker image


```sh
# 도커 이미지 삭제
docker images | grep -v regi | awk '{ print "docker rmi " $3}' | sh
```


### 방법2

- [도커 원격 private 레지스트리](https://dongle94.github.io/docker/docker-remote-private-registry/)
	- SSL 인증서 생성
		- key 생성
		- csr 생성
		- key 파일 암호 해제
		- config 파일 생성
		- crt 생성
		- SSL 생성
		- 기존 레지스트리 컨테이너 종료
		- 새로운 레지스트리 컨테이너 실행
		- 푸시 후 이미지 리스트 확인
		- curl로 확인


```sh
openssl genrsa -des3 -out server.key 2048
openssl req -new -key server.key -out server.csr

openssl rsa -in server.key -out server.key
echo subjectAltName=IP:172.16.6.77,IP:127.0.0.1 > extfile.cnf
openssl x509 -req -days 10000 -signkey server.key -in server.csr -out server.crt -extfile extfile.cnf

sudo cp ~/docker-registry/server.crt /usr/local/share/ca-certificates/
sudo update-ca-certificates



docker run -d -p 5000:5000 --restart=always --name my_registry \
	-v /home/krms/docker-registry/volume/:/data \
	-v /home/krms/docker-registry/certs/:/certs \
	-e REGISTRY_HTTP_ADDR=0.0.0.0:5000 \
	-e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/server.crt \
	-e REGISTRY_HTTP_TLS_KEY=/certs/server.key \
	registry:2.6


# 로컬 pc환경-> 도커레지스트리서버
docker images
	mY-image ...


docker tag my_image 172.16.6.77:5000/my_image:latest
docker push 172.16.6.77:5000/my_image:latest
```

when i try to connect to mariadb from dbeaver
i get the following error : 
Network unavailable due to certificate issue.
Try changing the setting `Use Windows trust store` in Preferences->Connections and restart DBeaver. It might help if you haven't overridden trust store.
javax.net.ssl.SSLHandshakeException:PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target



No connection could be made because the target machine actively refused it.
                                                                                    │



```sh
sudo apt install mysql-client-5.7
```

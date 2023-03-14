

## CI/CD 구축
- [0. 도커 레지스트리 생성](#0-도커-레지스트리-생성)
- [1. Gitlab 서버 생성](#1-gitlab-서버-생성)
- [2. TeamCity 서버 생성](#2-teamcity-서버-생성)
- [3. Gitlab 프로젝트 생성](#3-gitlab-프로젝트-생성)
- [4. TeamCity 프로젝트 생성](#4-teamcity-프로젝트-생성)


### 0. 도커 레지스트리 생성

1. 도커허브 계정 > private 리포지토리 생성

- TeamCity > Connections 추가
	- Registry Address: https://docker.io
	- Username/Password: 도커허브 계정정보
- TeamCity > Build Features에서 docker registry 추가

2. 도커 private 레지스트리 생성 (https://172.16.6.77:5000)

- [참고링크](https://dongle94.github.io/docker/docker-remote-private-registry/)
	- Registry Address: 172.16.6.77:5000
	- Username/Password: -
	- Insecure registry:
		- 도커 데몬 `insecure-registries` 옵션으로 HTTPS 인증서 우회하여 docker push
	- Secure registry 등록하기 위한 테스트
	- 로컬->도커레지스트리 연결 테스트
		- 원격 생성 .crt 인증서 다운로드 하여 인증서 추가
	- 팀시티->도커레지스트리 연결 테스트
		- 원격 생성 .crt 인증서 팀시티 우분투 서버에 설치
	- 도커 레지스트리 구동시(docker run), `--insecure-registry` 옵션은 보안에 취약 하므로, SSL 인증서를 발급하는 방법 적용
	- SSL 인증서로 허용된 클라이언트 PC에서만 docker push/pull 사용 가능

```sh
# 로컬-> 레지스트리 https 연결 우회
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


## TeamCity가 아닌 로컬-> 레지스트리 테스트
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

# 
sudo update-ca-certificates


docker run -d -p 5000:5000 --restart=always --name my_registry \
	-v /home/krms/docker-registry/volume/:/data \
	-v /home/krms/docker-registry/certs/:/certs \
	-e REGISTRY_HTTP_ADDR=0.0.0.0:5000 \
	-e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/server.crt \
	-e REGISTRY_HTTP_TLS_KEY=/certs/server.key \
	registry:2.6


No HTTP secret provided - generated random secret.
This may cause problems with uploads if multiple registries are behind a load-balancer.
To provide a shared secret, fill in http.secret in the configuration file
or set the REGISTRY_HTTP_SECRET environment variable


# 로컬 pc환경-> 도커레지스트리서버
docker images
	mY-image ...


docker tag my_image 172.16.6.77:5000/my_image:latest
docker push 172.16.6.77:5000/my_image:latest
docker pull 172.16.6.77:5000/my_image:latest
```


- 클라이언트 PC 인증서 적용
	- `Get x509: certificate signed by unknown authority`


```sh
scp -r krms@172.16.6.77:~/docker-registry/certs ~/

# 윈도우는 server.crt 더블클릭하여 직접설치
# docker 재시작

# 깃bash에서 확인
curl https://172.16.6.77:5000/v2/_catalog -k
	{"repositories":["my_image"]}
```

curl https://172.16.6.77:5000/v2/_catalog




### git bash에 .crt 인증서 추가

```sh
cat server.crt server.key > server.pem
openssl x509 -in server.crt -inform DER -out server.pem -outform PEM

```

error occurred while trying to remove image from docker repo by url:
https://172.16.6.77:5000/v2/:
PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target


- [Connecting to Insecure Registry](https://www.jetbrains.com/help/teamcity/configuring-connections-to-docker.html#Connecting+to+Insecure+Registry)

- TeamCity 서버 (바스티온 172.16.6.222)


- 로컬 .crt -> 바스티온 

```sh
# 로컬
scp -r server.crt krms@172.16.6.222:/home/krms

# 바스티온
cp -r /home/krms/server.crt /etc/docker/certs.d/172.16.6.77:5000

# 바스티온 -> 도커 레지스트리 서버
docker login 172.16.6.77:5000
```




### 1. Gitlab 서버 생성

```yml
version: '3.6'
services:
  gitlab:
    image: 'gitlab/gitlab-ce:latest'
    container_name: gitlab
    restart: always
    ports:
      - '8080:80'
      - '1443:443'
      - '1001:22'
    volumes:
      - '$GITLAB_HOME/config:/etc/gitlab'
      - '$GITLAB_HOME/logs:/var/log/gitlab'
      - '$GITLAB_HOME/data:/var/opt/gitlab'
    shm_size: '256m'
```

- `.env` 파일

```
GITLAB_HOME=/srv/gitlab/
```

### 2. TeamCity 서버 생성



```sh

# Default ${TEAMCITY_VERSION} is defined in .env file

# ./buildserver_pgdata - Posgres DB data
# ./data_dir - TeamCity data directory
# ./teamcity-server-logs - logs of primary TeamCity server
# ./agents/agent-1/conf - configuration directory for the first build agent
# ./agents/agent-1/conf - configuration directory for the second build agent
#
version: '3.6'
services:
  teamcity:
    image: jetbrains/teamcity-server:${TEAMCITY_VERSION}
    ports:
      - "8111:8111"
    volumes:
      - '$TEAMCITY_HOME/data_dir:/data/teamcity_server/datadir'
      - '$TEAMCITY_HOME/teamcity-server-logs:/opt/teamcity/logs'
    user: "root"
    shm_size: '128m'
    networks:
			- teamcity_network

  teamcity-agent-1:
    image: jetbrains/teamcity-agent:${TEAMCITY_VERSION}-linux-sudo
    privileged: true
    volumes:
      - '$TEAMCITY_HOME/agents/agent-1/conf:/data/teamcity_agent/conf'
    user: "root"
    environment:
      - DOCKER_IN_DOCKER=start
      - SERVER_URL=$TEAMCITY_SERVER_URL
    shm_size: '256m'
    networks:
			- teamcity_network

networks:
  teamcity_network:
    driver: bridge
    ipam:
      driver: default
      config:
        - subnet: 172.16.6.0/24
```

- `.env` 파일

```
TEAMCITY_HOME=/srv/teamcity/

TEAMCITY_VERSION=2022.04

# team city server url that agent would refer to
TEAMCITY_SERVER_URL=http://localhost:8111
```


- docker-compose.yml의 컨테이너에 네트워크 생성
	- 두 컨테이너 통신 및 외부 172.16.6.77:5000 액세스 가능

```
By adding the teamcity_network to the teamcity and teamcity-agent-1 services, you are creating a network bridge that allows these containers to communicate with each other over this network. Since the teamcity container is on this network and needs to access the external machine at 172.16.6.77:5000, the Docker network will handle the routing between the two.

In other words, the teamcity_network serves as a bridge network that connects the containers within it, and also provides a route to the external machine. When you specify a network for a container, Docker automatically adds a network interface to the container and assigns it an IP address within that network. This allows the containers on the same network to communicate with each other and also communicate with external machines on the same network.

By defining an external network, you are telling Docker that this network already exists and Docker should not try to create it. Therefore, when you start your Docker-compose file with the teamcity_network network, Docker will connect the containers to this pre-existing network, allowing them to communicate with each other and with external machines like the one at 172.16.6.77:5000.
```


### 3. Gitlab 프로젝트 생성

```sh
git clone https://devportal.kaonrms.com/konnect/YAML/on-premise/testgohttp.git

cd testgohttp
touch main.go
mkdir build
touch ./build/Dockerfile
go mod init devportal.kaonrms.com/konnect/YAML/on-premise/testgohttp
```

```go
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
```

```dockerfile
FROM golang:1.17-alpine as builder

WORKDIR /app

COPY . .

RUN go build -o main .

EXPOSE 8080

CMD ["./main"]
```

- dropdown > Admin > Application
	- Redirect URI: http://172.16.6.84:8111/oauth/gitlab/accessToken.html

### 4. TeamCity 프로젝트 생성

- TeamCity 프로젝트 설정
	- Administration > Project 페이지에서 다음 진행:
	- Create Project
		- Create Project From URL (공통계정 username/pw)
			- `{gitlab_url}.git`
		- Project name, VCS root, branch 등 설정
	- Build Configuration
		- Build Steps 추가
			1. set short hash (command line)
			2. docker build
			3. docker push
		- parameters 추가 'GitShortHash=%GitShortHash%'
		- Connections 추가
			- Project Settings > Connections > Add Connections
				- GitLab: appliation-id, secretKey (깃랩 > Application 생성시)
			- Project Settings > Connections > Add Connections
		- Build Features > docker registry (choose just added docker registry connection)
			- NOTE: docker-compose로 teamcity 서버 실행시, .yml에 network 정의필요-> docker registry(외부ip) 접근가능

- VCS Root name
	- https://devportal.kaonrms.com/konnect/cs/krms-mail-sender.git#refs/heads/master

- Fetch URL
	- {gitlaburl}.git

- Default branch
	- refs/heads/master

- Branch Specification
	- refs/heads/*

- Password/Personal Access Token
	- docker_rep/

- Build steps : CLI

```sh
#!/bin/bash

hash=%build.vcs.number%
shortHash=${hash:0:7}
echo "###teamcity[setParameter name='GitShortHash' value='$shortHash']"
```


- Build steps : Docker build
	- image:tag
	- 172.16.6.77:5000/my_image:%GitShortHash%
		
- Build steps : Docker push


```sh
sync
echo 1 > /proc/sys/vm/drop_caches
```





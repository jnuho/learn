

## TeamCity CI/CD 구축

- Gitlab 프로젝트 생성

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
			- [도커레지스트리 설정 방법](https://www.jetbrains.com/help/teamcity/configuring-connections-to-docker.html))
				1. Docker Registry (도커허브 https://docker.io)
				2. private 레지스트리 구축 (https://172.16.6.77:5000)
					- 참고: [docker-remote-private-registry 구축](https://dongle94.github.io/docker/docker-remote-private-registry)
				- 도커 레지스트리 구동시(docker run), `--insecure-registry` 옵션은 보안에 취약 하므로, SSL 인증서를 발급하는 방법 적용
				- SSL 인증서로 허용된 클라이언트 PC에서만 docker push/pull 사용 가능
		- Build Features > docker registry (choose just added docker registry connection)

### CI/CD 파이프라인

1. 도커허브

- Connections 추가
	- Registry Address: https://docker.io
	- Username/Password: 도커허브 계정정보
- Build Features에서 docker registry 추가

2. 도커 private 레지스트리 (https://172.16.6.77:5000)

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


### 클라이언트 PC 인증서 적용

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






### TeamCity

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

Hash=%build.vcs.number%
ShortHash=${Hash:0:7}
echo "###teamcity[setParameter name='GitShortHash' value='$ShortHash']"
```


- Build steps : Docker build
	- image:tag
	- 172.16.6.77:5000/my_image:%GitShortHash%
		
- Build steps : Docker push





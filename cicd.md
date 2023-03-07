
- Team City
	- Project 생성
	- Build Step 추가
		- cli (set short hash)
		- docker build
		- docker push
	- parameters 추가 'GitShortHash'
	- Connections > Add Connections > Docker Registry (:5050)


- On-Premise-Server

Public wifi	kaonmedia	172.16.6.77 테스트




Team city > (Root) KRMS3.0 > Krms Dev


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


but i still get error messages "http: server gave HTTP response to HTTPS client"
when i push my image from local to remote ubuntu server

please suggest the best 
free docker registry where i can push my local docker images
and pull images from into my local machine
i failed to setup my remote ubuntu machine as my own docker registry due to
docker in the remote machine not supporting https communication

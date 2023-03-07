
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

Gitlab (k8s_yaml)

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
	http.HandleFunc("/", func(w http.ResponseWriter,  r *http.Request) {
		fmt.Fprintf(w, "Hello World!")
	}
}
```

-> teamcity -(docker push)-> [Docker Registry]



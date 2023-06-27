
- Kubernetes
  - 컨테이너 오케스트레이션 플랫폼으로 컨테이너 어플리케이션 deploy, manage, scaling 프로세스 자동화
  - Kubernetes clusters : 리눅스 컨테이너 호스트를 cluster로 그룹화하고 관리
    - on-premise, public/private/hybrid clouds에 적용가능
    - 바른 스케일링이 필요한 cloud-native 어플리케이션에 적합한 플랫폼
  - 클라우드 앱 개발시 optimization에 유용
  - physical 또는 VM 클러스터에 컨테이너들을 scheduling 하고 run 할 수 있음
  - 클라우드 네이티브 앱을 '쿠버네티스 패턴'을 이용하여 쿠버네티스를 런타임 플랫폼으로 사용하여 만들수 있음
  - 추가 기능으로:
    - 여러호스트에 걸쳐서 컨테이너를 Orchestrate 할 수 있음
    - 엔터프라이즈 앱실행을 위해 리소스를 최대화하여 하드웨어 운용 가능
    - 어플리케이션 배포와 업데이트를 제어 및 자동화
    - Stateful 앱을 실행 하기 위해 스토리지를 마운트 하고 추가 가능
    - 컨테이너 애플리케이션과 리소스를 scaling 할 수 있음
  - 쿠버네티스는 다른 프로젝트들과 결합하여 효율적인 사용
    - Registry: Docker Registry
    - Networking
    - Telemetry
    - Security: LDAP, SELinux,RBAC, OAUTH with multitenancy layers
    - Automation
    - Services

- Kubernetes Architecture
  - [image1](https://devopscube.com/wp-content/uploads/2022/12/k8s-architecture.drawio-1.png)
  - [image2](https://www.redhat.com/rhdc/managed-files/kubernetes_diagram-v3-770x717_0_0_v2.svg)

- TERMS
  - Control Plane
    - 쿠버네티스 노드들을 컨트롤하는 프로세스의 집합
    - 여기서 모든 Task 할당이 이루어 짐
  - Node : 컨트롤 Plane으로 부터 할당된 Task를 수행하는 머신
  - Pod: 1개의 Node에 Deploy된 한개 이상의 컨테이너들
    - 파드에 있는 컨테이너들은 IP 주소, IPC (inter-process-communication), Hostname, 리소스
  - Replication 컨트롤러 : 몇개의 동일 pod 카피들이 클러스터에서 실행되어야 하는지 컨트롤
  - Service : Pods로부터 work definition을 분리함.
    - Kubernetes Service Proxy들이 자동으로 서비스 리퀘스트를 pod에 연결함
    - Cluster 내에서 어디로 움직이든 또는 replace 되더라도 자동으로 연결 됨.
  - Kubelet : 이 서비스는 노드에서 실행되며, 컨테이너 manifest를 읽고, 정의된 컨테이너들이 시작되고 작동하도록 함

- 동작원리
  - 클러스터 : 동작 중인 쿠버네티스 deployment를 클러스터라고 합니다.
    - 클러스터는 컨트롤 plane과 compute 머신(노드) 두가지 파트로 나눌 수 있습니다.
      - Control Plane + Worker nodes
    - 각각의 노드는 리눅스환경으로 볼 수 있으며, physical/virtual 머신입니다.
    - 각각의 노드는 컨테이너들로 구성된 pod들을 실행합니다.
    - 컨트롤러 플레인은 클러스터의 상태를 관리
      - 어떤 어플리케이션이 실행되고 있는지, 어떤 컨테이너 이미지가 사용 되고 있는지 등
      - Compute 머신은 실제로 어플리케이션과 워크로드들을 실행 합니다.
  - 쿠버네티스는 OS위에서 동작하면서 노드들위에 실행 중인 컨테이너 pod들과 interact 합니다.
    - 컨트롤러플레인은 admin으로부터 커멘드를 받아, Compute머신에 해당 커멘드들을 적용합니다.


### Docker

```sh
# PORTS: 컨테이너가 개방한 포트와, 호스트에 연결한 포트
#  외부에 노출하지 않을 떄는 항목내용 없음
docker stop NAME
docker rm NAME

docker rm -f NAME

# remove all stopped containers
docker container prune

# -a : 중지여부 상관없이 모든 컨테이너
# -q : ID만출력
docker ps -a -q

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

```sh
docker start myubuntu
docker exec -it myubuntu bash
# ehh0: 도커의 NAT IP 할당받은 인터페이스
# lo: 인터페이스
ifconfig
```


- Youtube Tutorial (TechWorld with Nana)

```
- Deployment > ReplicaSet > Pod > Container
	- use kubectl command to manage deployment

```sh
k get pod

k get services

k create deployment nginx-depl --image=nginx
k get deployment
k get pod
k get replicaset

k edit deployement nginx-depl
k get pod
	NAME                          READY   STATUS    RESTARTS   AGE
	nginx-depl-8475696677-c4p24   1/1     Running   0          3m33s
	mongo-depl-5ccf565747-xtp89   1/1     Running   0          2m10s

k logs nginx-depl-56cb8b6d7-6z9w6

k exec -it [pod name] -- bin/bash

k exec -it mongo-depl-5ccf565747-xtp89 -- bin/bash
k delete deployment mongo-depl
```


- microk8s 환경
  - https://microk8s.io/docs/getting-started
  - https://ubuntu.com/tutorials/install-a-local-kubernetes-with-microk8s?&_ga=2.260194125.1119864663.1678939258-1273102176.1678684219#1-overview


```sh
sudo snap install microk8s --classic

# 방화벽설정
# https://webdir.tistory.com/206

sudo usermod -a -G microk8s $USER
sudo chown -f -R $USER ~/.kube
su - $USER
microk8s status --wait-ready

vim .bashrc
  alias k='microk8s kubectl'
  alias helm='microk8s helm'

source .bashrc
```

- Microk8s, Ingress, metallb, nginx controller로 외부 서비스 만들기
  - 참고 문서
    - https://kubernetes.github.io/ingress-nginx/deploy/baremetal/
    - https://benbrougher.tech/posts/microk8s-ingress/
		- https://betterprogramming.pub/how-to-expose-your-services-with-kubernetes-ingress-7f34eb6c9b5a

- Ingress는 쿠버네티스가 외부로 부터 트래픽을 받아서 내부 서비스로 route할 수 있도록 해줌
  - 호스트를 정의하고, 호스트내에서 sub-route를 통해
  - 같은 호스트네임의 다른 서비스들로 route할 수 있도록 함
  - Ingress rule을 통해 하나의 Ip 주소로 들어오도록 설정
  - Ingress Controller가 실제 traffic route하며, Ingress는 rule을 정의하는 역할

- 이미지 만들기 -> Dockerhub에 push

```sh
# 이미지 만들기
cd learn/yaml/helloworld/docker
docker build -t server-1:latest -f build/Dockerfile .
docker tag server-1 jnuho/server-1
docker push jnuho/server-1
```

- simple-service.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hellok8s-deployment
  labels:
    app: hellok8s
spec:
  replicas: 1
  selector:
    matchLabels:
      app: hellok8s
  template:
    metadata:
      labels:
        app: hellok8s
    spec:
      containers:
      - name: hellok8s
        image: jnuho/server-1
        ports:
        - containerPort: 8081
---
apiVersion: v1
kind: Service
metadata:
  name: hellok8s-service
  # Use specific ip for metallb
  annotations:
    metallb.universe.tf/loadBalancerIPs: 172.16.6.100
spec:
  type: LoadBalancer
  selector:
    app: hellok8s
  ports:
  - port: 8081
    targetPort: 8081
```

```sh
k apply -f simple-service.yaml
k get svc
  NAME               TYPE           CLUSTER-IP      EXTERNAL-IP    PORT(S)          AGE
  kubernetes         ClusterIP      10.152.183.1    <none>         443/TCP          5d19h
  hellok8s-service   LoadBalancer   10.152.183.58   <none>         8081:31806/TCP   114s
```

```sh
# 사용중 ip인지 확인하기: 100-105
ping 172.16.6.100

microk8s enable metallb:172.16.6.100-172.16.6.105

# 로드밸런서 서비스의 IP가 metallb에 의해 할당됨
# 172.16.6.100:8081로 애플리케이션 접근

k get svc
  NAME               TYPE           CLUSTER-IP      EXTERNAL-IP    PORT(S)          AGE
  kubernetes         ClusterIP      10.152.183.1    <none>         443/TCP          5d19h
  hellok8s-service   LoadBalancer   10.152.183.58   172.16.6.100   8081:31806/TCP   114s

# 브라우저로 애플리케이션 접근 172.16.6.100:8081
curl 172.16.6.100:8081
```

- Kubernetes Component
  - Control plane
    - kube-apiserver
    - etcd
    - kube-scheduler
    - kube-controller-manager
    - cloud-controller-manager
  - Worker Nodes
    - kubelet
    - kube-proxy
    - Container runtime




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
  - 쿠버네트스는 다른 프로젝트들과 결합하여 효율적인 사용
    - Registry: Docker Registry
    - Networking
    - Telemetry
    - Security: LDAP, SELinux,RBAC, OAUTH with multitenancy layers
    - Automation
    - Services

- TERMS
  - 컨트롤 Plane
    - 쿠버네티스 노드들을 컨트롤하는 프로세스의 집합
    - 여기서 Task 할당이 이루어 짐
  - 노드 : 컨트롤 Plane으로 부터 할당된 Task를 수행하는 머신
  - 파드: 1개의 Node에 Deploy된 한개 이상의 컨테이너들
    - 파드에 있는 컨테이너들은 IP 주소, IPC (inter-process-communication), Hostname, 리소스
  - Replication 컨트롤러 : 몇개의 동일 pod 카피들이 클러스터에서 실행되어야 하는지 컨트롤
  - 서비스 : Pods로부터 수행할 work definition을 제거 함
  - Kubelet : 해당 서비스는 노드에서 작동하며, 컨테이너 manifest를 읽고, 정의된 컨테이너들이 시작하여 작동할 수 있도록 함

- 동작원리
  - 클러스터 : 동작 중인 쿠버네티스 deployment를 클러스터라고 합니다.
    - 클러스터는 컨트롤 plane과 compute 머신(노드) 두가지 파트로 나눌 수 있습니다.
    - 각각의 노드는 리눅스환경으로 볼 수 있으며, physical/virtual 머신입니다.
    - 각각의 노드는 컨테이너들로 구성된 pod들을 실행합니다.
    - 컨트롤러 플레인은 클러스터의 상태를 관리
      - 어떤 어플리케이션이 실행되고 있는지, 어떤 컨테이너 이미지가 사용 되고 있는지 등
      - Compute 머신은 실제로 어플리케이션과 워크로드들을 실행 합니다.
  - 쿠버네티스는 OS위에서 동작하면서 노드들위에 실행 중인 컨테이너 pod들과 interact 합니다.
    - 컨트롤러플레인은 admin으로부터 커멘드를 받아, Compute머신에 해당 커멘드들을 적용합니다.

<div>
<img src="https://www.redhat.com/cms/managed-files/kubernetes_diagram-v3-770x717_0_0_v2.svg?itok=Z6bFR9q1"
alt="쿠버네티스 클러스터" width="50%" height="100%">
</div>

- Docker

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


### Helm Chart

- Helm Chart 검토 배경

```
쿠버네티스 MSA 환경에서, 각 서비스별 YAML 파일로 컴포넌트(deployment, service)를
정의하고 있으며, 자원을 최초 생성하거나, 변경 사항이 생겼을때
YAML 파일 수정 후 각각 배포하는 반복적인 작업이 필요함.
```

- Helm Chart란?

```
Helm Chart 패키지 매니저는 이런 작업을 single authority 포인트를 통해
하나의 커맨드 라인으로 서비스들 변경사항을 한번에 배포할 수 있으며,
버전 관리를 통해, 배포건에 대한 손쉬운 rollback, update, delete 등의 작업이 가능합니다.
```



```sh
ls ./dc-repo
  dc-chart  dc-root  dc-config

    dc-repo
    ├── dc-chart
    │   ├── Chart.lock
    │   ├── charts
    │   │   ├── dc-config-0.1.0.tgz
    │   │   └── dc-root-0.1.0.tgz
    │   ├── Chart.yaml
    │   └── values.yaml
    ├── dc-config
    │   ├── Chart.yaml
    │   ├── templates
    │   │   ├── deployment.yaml
    │   │   └── service.yaml
    │   └── values.yaml
    └── dc-root
        ├── Chart.yaml
        ├── templates
        │   ├── deployment.yaml
        │   └── service.yaml
        └── values.yaml
```

- Chart.yaml

```yaml
apiVersion: v2
name: hellok8s
type: application
version: 0.1.0
appVersion: "1.0.0"
maintainer:
- email: junho.lee@kaongroup.com
  name: junho.lee
```

- templates/deployment.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}-deployment
  labels:
    app: hellok8s
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: hellok8s
  template:
    metadata:
      labels:
        app: hellok8s
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          ports:
            - name: http
              containerPort: {{ .Values.service.targetPort }}
              protocol: TCP
```

- templates/service.yaml

```yaml
apiVersion: v1
kind: Service
metadata:
  name: {{ .Release.Name }}-service
  annotations:
    metallb.universe.tf/loadBalancerIPs: 172.16.6.100
spec:
  selector:
    app.kubernetes.io/instance: {{ .Release.Name }}
  type: {{ .Values.service.type }}
  ports:
    - protocol: {{ .Values.service.protocol | default "TCP" }}
      port: {{ .Values.service.port }}
      targetPort: {{ .Values.service.targetPort }}
```

- templates/configmap.yaml

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-index-html-configmap
  namespace: default
data:
  index.html: |
    <html>
    <h1>Welcome</h1>
    </br>
    <h1>Hi! I got deployed in {{ .Values.env.name }} Environment using Helm Chart </h1>
    </html
```


- values.yaml

```sh
replicaCount: 1

image:
  repository: jnuho/server-1
  tag: "latest"
  pullPolicy: IfNotPresent

service:
  name: hellok8s
  type: LoadBalancer
  port: 8081
  targetPort: 8081

env:
  name: dev
```

- Validate the Helm Chart

```sh
helm lint ./hellok8s-chart

# generate with substituted values
helm template .

# pretend to install the chart to the cluster and show errors
helm install --dry-run my-release hellok8s-chart
```

- Deploy the Helm chart

```yaml
helm install frontend hellok8s-chart
```

- Helm Upgrade & Rollback

```yaml
helm upgrade frontend hellok8s-chart
helm rollback frontend
```

- Package the Helm Release

```sh
# package into .tgz file
helm package hellok8s-chart

```

- Uninstall the Helm Release

```sh
# purge resources and uninstall added helm release
helm uninstall frontend
```

- Trouble Shooting

```sh
k get all -n krms
k describe pod dc-config-7ff748777-28wpz -n krms

# https://github.com/containerd/cri/blob/master/docs/registry.md
vim /etc/containerd/config.toml
```


- Test

```sh
# access https://192.168.0.16:10443
microk8s enable dashboard
microk8s dashboard-proxy

# The containerd daemon used by MicroK8s is configured
# to trust this insecure registry.
# To upload images we have to tag them with
# localhost:32000/your-image before pushing them
microk8s enable registry
docker pull nginx
docker tag nginx localhost:32000/mynginx
docker push localhost:32000/mynginx

curl http://localhost:32000/v2/_catalog
	{"repositories":["mynginx"]}

helm create dc-chart
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo search bitnami | grep rabbitmq

# tree
dc-repo
├── dc-chart
│   ├── Chart.yaml
│   └── values.yaml
├── dc-config
│   ├── Chart.yaml
│   ├── templates
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   └── values.yaml
└── dc-root
    ├── Chart.yaml
    ├── templates
    │   ├── deployment.yaml
    │   └── service.yaml
    └── values.yaml

git clone $REPO/dc-repo.git
cd dc-repo
helm dep build dc-chart
helm install dc-chart ./dc-chart
helm upgrade dc-chart ./dc-chart

k get all -n krms
```


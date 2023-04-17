
### Helm Chart

- Why use Helm Chart?

```
MSA 환경에서 쿠버네티스는 각 서비스별 YAML 파일로 컴포넌트(deployment, service, …)를 정의하여 자원을 최초 생성하거나, 변경 사항이 생겼을때, YAML 파일 수정 후 커맨드를 통해 직접 배포하는 반복적인 작업이 필요 하다.

Helm Chart는 YAML의 묶음을 패키지화 하여, 하나의 authority 포인트로 관리한다.
또한, 패키지 버전 관리를 통해, 배포건에 대한 rollback, update, delete 등의 작업이 가능하다.
```

- Install Helm Chart(OS)
  - Prerequisite:
    - A working Kubernetes cluster

```sh
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh

# microk8s 환경
microk8s enable helm3
```


vim .bashrc
  alias k='microk8s kubectl'
  alias helm='microk8s helm'


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

- Helm Commands

```sh
# 템플릿에 values.yaml에서 정의한 값을 대입하여 실제 Render된 결과 출력
helm template parent-chart/

# 차트 포맷 등 오류 검증
cd dc-repo
helm lint parent-chart/

# --dry-run로 클러스터에 실제 차트 설치 없이
# 실행 될 결과를 출력하여 에러로그 등을 확인
helm install --dry-run dc-chart parent-chart

# 차트를 생성하고, 자원들을 deploy
helm install dc-chart parent-chart/

# 차트에 변경사항(템플릿 혹은 value 정의 값들 등을 반영)
helm upgrade dc-chart parent_chart/

# 차트 히스토리 조회
helm history dc-chart

# 특정 버전으로 차트를 롤백: 록백시에도 버전 1씩 증가
helm rollback dc-chart VERSION_NO

# Uninstall the Helm Release
helm uninstall dc-chart

# 생성된 자원 확인하기
k get all -n krms
k describe pod dc-config-7ff748777-28wpz -n krms

# Test access https://192.168.0.16:10443
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
helm dep build parent-chart
helm dep update parent-chart
helm install dc-chart ./parent-chart
helm upgrade dc-chart ./parent-chart

k get all -n krms
```


- Library Charts

```sh
helm create lib-chart
rm -rf lib-chart/templates/*
rm -f lib-chart/values.yaml

# Write library template
vim lib-chart/templates/_deployment.yaml
vim lib-chart/templates/_service.yaml

# Set type: library
vim lib-chart/Chart.yaml
```

- Use library chart from parent chart

```sh
cd parent-chart
```


```sh
cd dc-repo
helm dep update parent-chart
helm install dc-chart ./parent-chart --debug --dry-run
helm install dc-chart ./parent-chart
```


- 2023-04-07 Demo

```sh
curl -fsSL -o get_helm.sh \
  https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh

helm version
helm -–help
helm list



# 1. Helm Chart 저장소에서 다운받아 사용
# Helm Chart들이 패키지로 저장되어 있는 bitnami 저장소를
# 추가하고, 원하는 chart (ex. nginx)를 다운로드 할 수 있습니다.
helm repo add bitnami https://charts.bitnami.com/bitnami

# 차트 검색 (최신 10개 조회)
helm search repo bitnami/nginx -l

# 특정 버전의 nginx 차트를 설치
helm install my-nginx bitnami/nginx --version 13.2.10

# 특정 버전의 nginx 차트로 업그레이드
helm upgrade my-nginx bitnami/nginx --version 13.2.30

# 차트 업그레이드 (서비스 포트 변경 : 디폴트 80->8081)
helm inspect values bitnami/nginx | less -R
helm upgrade my-nginx bitnami/nginx --set service.ports.http=8081




# 2. Chart 디렉토리 구조를 직접 정의하여 차트 구성
# 디폴트 차트 디렉토리 생성 (공통 파일 및 YAML 파일 생성)
# 환경에 맞게 커스텀 파일 생성 및 디렉토리 구조 수정
helm create test-chart

# 차트 포맷 등 오류 검증
helm lint test-chart

# --dry-run로 클러스터에 실제 차트 설치 없이
# 실행 될 결과를 출력하여 에러로그 등을 확인
helm install --dry-run my-chart ./test-chart


# 차트를 생성하고, 자원들을 deploy
helm install my-chart test-chart/

# 차트에 변경사항(템플릿 혹은 value 정의 값들 등을 반영)
helm upgrade my-chart test-chart/

# 차트 히스토리 조회
helm history my-chart

# 특정 버전으로 차트를 롤백: 록백시에도 버전 1씩 증가
helm rollback my-chart [Version NO.]

# Uninstall the Helm Release (자원도 함께 삭제)
helm uninstall my-chart

# 생성된 자원 확인하기
kubectl get all -n krms






# krms 데모
cd dc-repo

helm dependency build parent-chart/
helm dep update parent-chart/

# --dry-run로 클러스터에 실제 차트 설치 없이
# 실행 될 결과를 출력하여 에러로그 등을 확인
helm install --dry-run dc-chart parent-chart/

# 차트를 생성하고, 자원들을 deploy
helm install dc-chart parent-chart/

# 차트에 변경사항(템플릿 혹은 value 정의 값들 등을 반영)
helm upgrade dc-chart parent_chart/

# 차트 히스토리 조회
helm history dc-chart

# 특정 버전으로 차트를 롤백: 록백시에도 버전 1씩 증가
helm rollback dc-chart VERSION_NO

# Uninstall the Helm Release
helm uninstall dc-chart

# 생성된 자원 확인하기
k get all -n krms
k describe pod dc-config-7ff748777-28wpz -n krms

# Test access https://192.168.0.16:10443
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


```


### Helm Chart

1. Helm 차트 검토 배경

```
MSA 환경에서, 쿠버네티스는 클러스터의 컴포넌트 또는 매니패스트를 .yaml 파일로 정의합니다.
이 파일은 컴포넌트를 정의하는 명세서 역할을 하며, 컴포넌트로는 컨테이너 외부 통신을 위한
인터페이스를 정의하는 Service, 컨테이너와 관련된 정보를 정의하는 Deployment 등이 있습니다.

CLI 툴인 kubectl은 쿠버네티스 API를 호출하여 .yaml 파일에 해당하는 객체를
생성, 삭제, 수정 등의 작업을 수행합니다. 클러스터 내 서비스 개수가 많아짐에 따라,
관리해야할 .yaml 파일이 많아지고, kubectl로 컴포넌트를 개별적으로 생성, 수정하는
작업의 효율이 떨어집니다.

Helm은 .yaml 파일들의 공통된 내용을 template으로 정의하여 서비스 또는 배포환경에 맞는
values.yaml 값들을 참조하여, 다수의 컴포넌트를 하나의 helm 커맨드로 생성 및 수정 할 수 있습니다. 또한, 애플리케이션을 하나의 Chart로 패키지화 하여, 설치, 업그레이드, 삭제 할 수 있는, 관리포인트를 제공합니다.
```

1. Helm Chart 검토 배경

```
쿠버네티스 환경에서, 각 서비스별 YAML 파일로 컴포넌트(deployment, service)를
정의하고 있으며, 자원을 최초 생성하거나, 변경 사항이 생겼을때
YAML 파일 수정 후 kubectl 커맨드를 통해 개별 배포하는 반복적인 작업이 필요합니다.
```

1.1 Helm Chart란?

```
Helm Chart 패키지 매니저는 이런 작업을 single authority 포인트를 통해
하나의 커맨드 라인으로 서비스들 변경사항을 한번에 배포할 수 있으며,
버전 관리를 통해, 배포건에 대한 손쉬운 rollback, update, delete 등의 작업이 가능합니다.
```

1.2. helm과 kubectl 커맨드 역할

```
Helm은 kubectl로 각 서비스 개별적으로 수행하던 자원 생성, 수정등의 기능을
대체함과 동시에, Chart 패키지의 버전관리 및 롤백 등의 역할을 합니다. 
그외에, 자원의 조회 및 로그 확인, 컨테이너 내부 진입 등 디버깅 및 자원조회는
기존에 사용하던 kubectl로 수행 합니다. 이와 같이 목적에 따라, helm과 kubectl 커맨드를 사용하게 됩니다.
```

2. Helm 차트 설치

2.1. 선행 조건

2.1.1. 쿠버네티스 클러스터 구성

Helm 차트를 설치하기전에 쿠버네티스 클러스터를 구성합니다. EKS, GKE, AKS 등 관리형 쿠버네티스 서비스,
또는 On-premise 또는 EC2 인스턴스에 microk8s 경량화 쿠버네티스로 클러스터를 구성합니다.
본문서는 Amazon EC2 우분투 Linux머신에 microk8s를 설치하여, 클러스터를 구성하였습니다.

2.2.2. kubectl CLI 설치

```sh

# microk8s 사용 시 기본적으로 설치 되어 있음.
microk8s kubectl version

# 그외 클러스터 구성 후 CLI 설치
curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.26.4/2023-05-11/bin/linux/amd64/kubectl
chmod +x ./kubectl
mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$HOME/bin:$PATH
echo 'export PATH=$HOME/bin:$PATH' >> ~/.bashrc
kubectl version --short --client
```


2.2.  설치 가이드

본 문서의 가이드는, Ubuntu Linux OS 환경에서 설치 하였습니다.
CentOS에서도, 설치가 가능하며 snap 패키지 매니저 설치가 선행되어야 합니다.

- snap 설치

```sh
# 1. 우분투 환경
sudo apt update
sudo apt install snapd

# 2. CentOS 환경
sudo dnf install epel-release -y
sudo dnf update
sudo dnf -y install snapd
```

- microk8s 설치 (with snap 패키지)

```sh
# MicroK8s 설치
sudo snap install microk8s --classic --channel=1.27

# 그룹에 조인
sudo usermod -a -G microk8s $USER
sudo chown -f -R $USER ~/.kube

# 쿠버네티스 클러스터 상태 조회
microk8s status --wait-ready

# 쿠버네티스 노드 조회
microk8s kubectl get nodes
```


- helm 설치

```sh
# 1. shell 스크립트로 설치
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh

# 2. microk8s 환경
microk8s enable helm3
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

2. Helm 커맨드


위에서 디렉토리 구조가 만들어졌다면, helm install 커맨드로 차트의 '릴리즈'를 설치할 수 있습닌다.

설치하기에 앞서, 서비스간 디펜던시가 있다면 디펜던시 빌드를 해야하며,
차트의 디렉토리 구조나, 템플릿등에 문제가 없는지 검증 및 
생성될 매니패스트 결과를 yaml로 미리 출력 해 볼 수 있습니다.


```sh
# parent-chart의 Chart.yaml에 정의된 서비스들의 디펜던시를 참고하여,
# child 서비스들과 lib-chart를 서브차트 패키지 .tgz로 빌드
helm dep build parent-chart/

# 빌드 후 차트의 변경사항 (values.yaml 또는 서비스 추가/수정/삭제가 발생)을 업데이트
helm dep update parent-chart/

# 차트 포맷 등 오류 검증
helm lint parent-chart/

# 템플릿에 values.yaml에서 정의한 값을 대입하여 실제 Render된 결과 출력
helm template parent-chart/

# helm template과 비슷하지만, render된 객체들이 valid한 쿠버네티스 객체인지 여부도 검증
# 차트 설치 없이 실행 될 결과를 출력하여 에러로그 등을 확인
helm install --dry-run my-release parent-chart

# 차트에 해당하는 release를 생성하고, 쿠버네티스 자원 생성
helm install my-release parent-chart/

# 차트 업그레이드 (템플릿 혹은 value 정의 값들 등을 반영) 
# 업그레이드 전 helm dep update parent-chart
helm upgrade my-release parent-chart/

# 차트 히스토리 조회
helm history my-release

# 특정 버전으로 차트를 롤백: 록백시에도 버전 1씩 증가
helm rollback my-release VERSION_NO

# Uninstall the Helm Release
helm uninstall my-release

# helm diff 플러그인 설치
helm plugin install https://github.com/databus23/helm-diff

# values.yaml 변경 후 업그레이드를 하고 helm diff로 변경사항 확인
helm dep update my-release parent-chart
helm upgrade my-release parent-chart
helm diff revision my-release 1 2




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

helm dep build parent-chart/
helm dep update parent-chart/

# --dry-run로 클러스터에 실제 차트 설치 없이
# 실행 될 결과를 출력하여 에러로그 등을 확인
helm install --dry-run dc-chart parent-chart/

# 차트를 생성하고, 자원들을 deploy
helm install dc-chart parent-chart/

# 차트에 변경사항(템플릿 혹은 value 정의 값들 등을 반영)
helm upgrade dc-chart parent-chart/

# 차트 히스토리 조회
helm history dc-chart

# 특정 버전으로 차트를 롤백: 롤백시에도 버전 1씩 증가
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


- helm repo 활용하기

```sh
# helm package CHART_NAME --version=MAJOR.MINOR.PATCH
cd tst-helm
helm package parent-chart
  parent-chart-0.1.0.tgz

cp parent-chart-0.1.0.tgz ~/test
cd ~/test
helm repo index .

# helm push [chart-package] [remote] [flags]
helm push parent-chart-0.1.0.tgz \
  oci://13.209.144.77/tst-project

helm push parent-chart-0.1.0.tgz \
  oci://admin:kaon.1234@13.209.144.77/tst-project
```

Missing a way to configure, release, version, rollback and inspect the deployments.

Helm Chart 개요
Helm Chart 설치
Helm Chart 커맨드

Helm Chart 데모

Helm Chart


Helm relies on kubectl to interact with Kubernetes clusters.
When you install Helm, it uses the kubectl configuration to connect to the cluster
Helm will automatically use the same Kubernetes cluster configuration as kubectl.




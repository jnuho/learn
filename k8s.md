


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


- Kubenetes [tutorial](https://youtu.be/X48VuDVv0do)
- install [microk8s](https://microk8s.io/docs/getting-started)

```sh
sudo snap install microk8s --classic --channel=1.26
sudo usermod -a -G microk8s $USER
sudo chown -f -R $USER ~/.kube
su - $USER
microk8s status --wait-ready

# alias
snap alias microk8s.kubectl k
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
	NAME                          READY   STATUS              RESTARTS   AGE
	nginx-depl-56cb8b6d7-6z9w6    1/1     Running             0          3m49s
	nginx-depl-8475696677-c4p24   0/1     ContainerCreating   0          5s

k logs nginx-depl-56cb8b6d7-6z9w6

k exec -it [pod name] -- bin/bash
k exec -it [pod name] -- bin/bash

k get pod
	NAME                          READY   STATUS    RESTARTS   AGE
	nginx-depl-8475696677-c4p24   1/1     Running   0          3m33s
	mongo-depl-5ccf565747-xtp89   1/1     Running   0          2m10s

k exec -it mongo-depl-5ccf565747-xtp89 -- bin/bash
k delete deployment mongo-depl
```


- yaml configuration


```

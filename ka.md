

- wifi RMS-INTRA-5G
kaon.1234


- AWS Account:
kaon.krms@kaonmedia.com
Kaon.wa!2@


- AWS Account (junho.lee)
junho.lee@kaonmedia.com
Kaon.wa!2@

AWS Account:
01. https://kaon-buckeye.signin.aws.amazon.com/console
02. https://kaon-kus.signin.aws.amazon.com/console
03. https://kaon-evln.signin.aws.amazon.com/console
04. https://kaon-kacs.signin.aws.amazon.com/console
05. https://kaon-krms.signin.aws.amazon.com/console
06. https://kaon-kams.signin.aws.amazon.com/console
07. https://kaon-master.signin.aws.amazon.com/console
08. https://kaon-management.signin.aws.amazon.com/console

No       Account ID           AWS Account Name
1         088356671508    kaon-krms
2         197642889365    kaon-management
3         341120546701    kaon-evln
4         352400234461    kaon-kus
5         424515005434    kaon-kacs
6         434885143221    kaon-master
7         641834490695    kaon-kams
8         805028808410    kaon-buckeye

https://kaon-krms.signin.aws.amazon.com/console
https://kaon-management.signin.aws.amazon.com/console
https://kaon-evln.signin.aws.amazon.com/console
https://kaon-kus.signin.aws.amazon.com/console
https://kaon-kacs.signin.aws.amazon.com/console
https://kaon-master.signin.aws.amazon.com/console
https://kaon-kams.signin.aws.amazon.com/console
https://kaon-buckeye.signin.aws.amazon.com/console

- 팀시티

https://www.jetbrains.com/teamcity/buy/#on-premises?licence=enterprise
kaon.rdk@gmail.com / Kkft.!234

- GCP Account:

junho.lee@kaonmedia.com


- CI
https://devportal.kaonrms.com/
	

- CD
http://teamcity.kaonrms.com:8111/

krms 3.0 -> GCP
krms 3.1 -> AWS

etv-krms.kaonmedia.com


```sh

route delete 192.168.148.0 mask 255.255.128.0
route add 192.168.148.0 mask 255.255.255.0 172.16.6.79 -p

route delete 192.168.148.0 mask 255.255.255.0
route add 192.168.148.0 mask 255.255.255.0 172.16.6.79 -p

route print

ping 192.168.148.1
```



- DBeaver
- teamcity
- Docker registry
- AWS cli + SSH
krms-dev -> etv-bastion-dev-001


ssh mgtkrms01
ssh mgtkrms02
ssh mgtkrms03
ssh ESXi
ssh krms-dev
ssh krms-server-01
ssh krms-git
ssh krms-xmpp
ssh krview-dev
ssh wifi

- 


route add 172.16.6.0 netmask 255.255.255.0 gw 198.168.148.1



VMWare
https://172.16.6.107/ui/#/login
- gitlab : 
- teamcity + agent : 
- registry : 172.16.6.77





T16 Gen1
12th Gen Intel(R) Core(TM) i7-1260P   2.10 GHz
16GB


/etc/netplan/*.yaml

ip address 172.16.6.76
netmask 255.255.255. 0
default gateway 172.16.6.1
dns search domain


- 77: docker registry(docke)
- 77: gitlab
- 77: teamcity agent01
- 77: teamcity agent02
- 76: microk8s (helm chart)
- 76: teamcity server
- 80: -
- 81: -

1. teamcity ssh exec
2. helm chart


- 2023-04-28 device-fe-api (5003)
  - etv-dev.krms.kaonmedia.com (AWS istio)
  - krms-dev.kaonrms.com (nginx)

/api.kaonrms.com/auth/v1/token net::ERR_CERT_DATE_INVALID
krms-dev.kaonrms.com/auth/v1/token net::ERR_CERT_DATE_INVALID
dev-api.kaonrms.com/auth/v1/token

- 2023.05.02 nginx
  - 서비스
    - /device-api/v1
    - fe-device-api
    - 3005

- 2023.05.02 
  - console.kaonrms.com, dev-console.kaonrms.com
  - GCP Cloud DNS  TXT


```sh
sudo certbot certonly --manual --preferred-challenges dns -d "*.kaonrms.com"
# 인증서 정보
openssl x509 -text -noout -in fullchain.pem
```


```sh
# Google cloud sdk 설치 후: dev-kaonrms, stage-kaonrms에 적용
gcloud components install gke-gcloud-auth-plugin
gcloud container clusters get-credentials krms-cluster-ane1 --zone asia-northeast1-c --project kaonrms-2020072201

kubectl get secret -n istio-system istio-ingressgateway-certs -o yaml > istio-ingressgateway-certs_20230502.yaml

kubectl get secret -n istio-system istio-ingressgateway-certs
kubectl delete -n istio-system secret istio-ingressgateway-certs
kubectl create -n istio-system secret tls istio-ingressgateway-certs --key=./privkey.pem --cert=./fullchain.pem

kubectl get pod -n istio-system -l istio=ingressgateway
kubectl delete pod -n istio-system -l istio=ingressgateway
```

Name:   console.kaonrms.com
Address: 35.196.173.169

Name:   dev-console.kaonrms.com
Address: 34.84.236.33


- 개발서버 인증서 자동갱신을위한 certbot 컨테이너 생성
  - 


dev-machine
krms-dev.kaonrms.com 


/bin/sh -c 'trap exit TERM; while :; do certbot renew; sleep 12h & wait $${!}; done;'




https://argocd-dev.kaonrms.com



### [EKS 실습](https://catalog.us-east-1.prod.workshops.aws/workshops/9c0aa9ab-90a9-44a6-abe1-8dff360ae428/ko-KR)

- IAM
  - User
    - username : testcluster-001
    - password : Kaon.1234
  - Role
    - Name: testcluster-001-AmazonEKSClusterRole
    - Policy: AmazonEKSClusterPolicy, AmazonEKSServicePolicy
- Subnet




- ClusterName: testcluster-001
- CloudFormation Stack : testcluster-001-Stack-VPC-Private-Public

VpcBlock 172.32.0.0/16
PublicSubnet01Block 172.32.0.0/18
PublicSubnet02Block 172.32.64.0/18
PrivateSubnet01Block 172.32.128.0/18
PrivateSubnet02Block 172.32.192.0/18

VpcBlock	172.33.0.0/16
00000000 (0)  - 00111111 (63)
01000000 (64) - 01111111 (127)
10000000 (128) - 10100000 (191)
11000000 (192) - 11111111 (255)




- krms-dev
  - teamcity-agent 2,3 docker 기동 중
  - teamcity-server + agent 1 : 패키지로 설치되어, 실행 중


일단 예산 신청이 반영되면 
은행명: 자동이체
계좌번호: -900
업체명: 법인카드(현대)


eksServiceTeam


tivo
- teamcity-build config 추가
- harbor projects 추가














{
        "Version": "2008-10-17",
        "Id": "PolicyForCloudFrontPrivateContent",
        "Statement": [
            {
                "Sid": "AllowCloudFrontServicePrincipal",
                "Effect": "Allow",
                "Principal": {
                    "Service": "cloudfront.amazonaws.com"
                },
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::demo-krview/*",
                "Condition": {
                    "StringLike": {
                        "aws:SourceArn": [
                          "arn:aws:cloudfront::641834490695:distribution/E1W3WFI863J5RU",
                          "arn:aws:cloudfront::641834490695:distribution/E3DQNBRS5MMKHK"
                        ]
                    }
                }
            }
        ]
      }
      



https://d1opu4ywthqcdi.cloudfront.net/aaa_dev.txt
https://ddotcxgmy7a5g.cloudfront.net/aaa_stage.txt

https://krview-cdn.rmsview.com/dev/aaa_dev.txt
https://krview-cdn.rmsview.com/stage/aaa_stage.txt
https://krview-cdn.rmsview.com/prd/dns.png

bastion에 etv krmsview.com ingress 삭제처리
- console
- cwmp

1. etv
2. stage
  - demo
  - stage
3. prd



- dev 용 클러스터 (etv): 권한
- stage 용 클러스터 생성


- 팀시티 결제
- EKS 



1 loadbalancer controller
2 istio nlb alb
3 ingress



krms3.1-aws-console



- TeamCity

FE-WEB (console/xperi-stage/etisalat-stage)
  * build:
    yarn install,run
    docker build,push
      -> https://admin@krms-dev.kaonrms.com:10443
        (krms-dev 서버 10443 도커 레지스트리)
    docker pull, docker-compose down, up (*SSH Exec - test_server_rsa)
    https://devportal.kaonrms.com/konnect/service/front-end/krms-fe-web.git#refs/heads/master

  * build-onp-etv:
    yarn install,run
    docker build,push
      -> https://admin@krms-dev.kaonrms.com:10443
      -> https://tc@devportal.kaonrms.com:5050 (gitlab container)
      https://devportal.kaonrms.com/konnect/service/front-end/krms-fe-web.git#refs/heads/master (1)

FE
  Krms Fe Api (console/xperi-stage/etisalat-stage)
  FE Web Socket (core)
  Fe Admin (core)
  Fe Device Api (core)
  Krms Fe Auth (core)

  [_NEW_] fe-partner-api (console/xperi-stage/etisalat-stage)
  [_NEW_] fe-statistics (core)

CS
  Krms Mail Sender
  Krms Scheduler
  Krms Service Watcher

Data
IDLs
SFG
SG
Task
device core
device frontend




rmsinfo-nlb-stage-console
rmsinfo-nlb-stage-xperi
rmsinfo-cwmp-stg-console
rmsinfo-cwmp-stg-xperi
rmsinfo-dashboard-stg-console
rmsinfo-dashboard-stg-xperi



xmpp:5222

- krms31-stage
  - SG : sg-0434e49aa7f54c6c5


3008
location /partner-api/v1/


testcluster-EKS-VPC-Stack-001-VPC-Only-Public


Subnet01Block	172.34.64.0/18	-
Subnet02Block	172.34.128.0/18	-
Subnet03Block	172.34.192.0/18	-
VpcBlock	172.34.0.0/16







```sh
[ec2-user@ip-172-34-72-189 003.fe-web]$ k get all -n console
NAME                               READY   STATUS    RESTARTS   AGE
pod/df-mtp-xmpp-59db9656bd-lmqdd   2/2     Running   0          3h48m
pod/fe-web-8548b64fd5-mcgpg        2/2     Running   0          3h48m

NAME                  TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
service/df-mtp-xmpp   ClusterIP   10.100.141.200   <none>        5222/TCP       4h10m
service/fe-web        NodePort    10.100.201.37    <none>        80:31647/TCP   4h9m

NAME                          READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/df-mtp-xmpp   1/1     1            1           4h9m
deployment.apps/fe-web        1/1     1            1           4h8m

NAME                                     DESIRED   CURRENT   READY   AGE
replicaset.apps/df-mtp-xmpp-59db9656bd   1         1         1       4h9m
replicaset.apps/fe-web-8548b64fd5        1         1         1       4h8m


kubectl label namespace xperi istio-injection=enabled
001.df: dr은 적용 x

kubectl label namespace etisalat istio-injection=enabled


# ,5222:32352/TCP

k get svc -n istio-system | grep xperi
k get all -n xperi
```

- console

telnet ip-172-34-174-17.ap-northeast-2.compute.internal 31395
telnet ip-172-34-67-119.ap-northeast-2.compute.internal 31395

- xperi

telnet ip-172-34-174-17.ap-northeast-2.compute.internal 32352
telnet ip-172-34-67-119.ap-northeast-2.compute.internal 32352

- etisalat

telnet ip-172-34-174-17.ap-northeast-2.compute.internal 32193
telnet ip-172-34-67-119.ap-northeast-2.compute.internal 32193

- 콘솔 제외한 서비스 : xperi-stage-xxx
  


003.etisalat-stage




./istioctl upgrade -f istio.yaml
kubectl label namespace core istio-injection=enabled
kubectl label namespace etisalat istio-injection=enabled

etisalat-stage.rmsinfo.net



telnet etisalat-stage-xmpp.rmsinfo.net 5222




- Helm Chart
  - deployment
  - service
  - vs
  - dr

- Harbor Registry
  - krms3.1
  - krms3.1-onp-etv
  - krms3.1-aws-console
  - krms3.1-aws-core
  - krms3.1-aws-xperi-stage

- TeamCity
  - Build (krms3.1)
  - Build onp etv (etv)
  - Build (core)

1. Registry Tags (GitLab URI path)
  - ProjectName: 팀시티 프로젝트 이름 (krms3.1)
  - GitlabProjectServiceDomainName	konnect/service/back-end
  - AppName	krms-fe-api
  - ServiceDomainName	back-end


devportal.kaonrms.com:5050/konnect/[refer-to-git-registry-url]/%build.counter%.%teamcity.build.branch%.%GitShortHash%
devportal.kaonrms.com:5050/konnect/[refer-to-git-registry-url]:latest

devportal.kaonrms.com:5050/konnect/scheduler/krms-mail-sender:%build.counter%.%teamcity.build.branch%.%GitShortHash%
devportal.kaonrms.com:5050/konnect/scheduler/krms-mail-sender:latest
krms-dev.kaonrms.com:10443/krms3.1-aws-console/cs/krms-mail-sender:%GitShortHash%
krms-dev.kaonrms.com:10443/krms3.1-aws-console/cs/krms-mail-sender:latest

2. Registry Tags (Harbor)
  - 팀시티프로젝트명/서비스


- krms3.1

krms-dev.kaonrms.com:10443/[refer-to-harbor-registry-url]:%build.counter%.%teamcity.build.branch%.%GitShortHash%
krms-dev.kaonrms.com:10443/[refer-to-harbor-registry-url]:latest





devportal.kaonrms.com:5050/konnect/scheduler/krms-mail-sender:%build.counter%.%teamcity.build.branch%.%GitShortHash%
devportal.kaonrms.com:5050/konnect/scheduler/krms-mail-sender:latest
krms-dev.kaonrms.com:10443/krms3.1-aws-console/cs/krms-mail-sender:%build.counter%.%teamcity.build.branch%.%GitShortHash%
krms-dev.kaonrms.com:10443/krms3.1-aws-console/cs/krms-mail-sender:latest

devportal.kaonrms.com:5050/%GitlabProjectServiceDomainName%/%AppName%:%build.counter%.%teamcity.build.branch%.%GitShortHash%
devportal.kaonrms.com:5050/%GitlabProjectServiceDomainName%/%AppName%:latest
krms-dev.kaonrms.com:10443/%ProjectName%/%ServiceDomainName%/%AppName%:%build.counter%.%teamcity.build.branch%.%GitShortHash%
krms-dev.kaonrms.com:10443/%ProjectName%/%ServiceDomainName%/%AppName%:latest

- 복사, VCS 브랜치 수정, ProjectName수정
  -> krms3.1-aws-console
  - tag immutability: disabled
  - scan on push: 
  - kms encryption: 



aws ecr create-repository \
  --repository-name krms3.1-aws-console



- stage 환경 구축
  - 추가되는 teamcity, ecr, harbor 등 정보 업데이트 하기
  - https://docs.google.com/spreadsheets/d/190FwrNGrfv-7xlhLQiCZFiK1onQvF1g7LNeJXbQNbXY/edit#gid=0


088356671508.dkr.ecr.ap-northeast-2.amazonaws.com/krms3.1-aws-etv
088356671508.dkr.ecr.ap-northeast-2.amazonaws.com


krms3.1-aws-core-ecr-push
krms3.1-aws-core/**
krms3.1-aws-core

- 획인: gitlab, harbor, ecr(harbor replicate)


k create ns krms
k label namespace krms istio-injection=enabled





CS
  Krms Mail Sender
  Krms Scheduler
  Krms Service Watcher
Data
FE
FE-WEB
IDLs
SFG Service
SG
Task
device core
device frontend








- 2023-05-23
- L4 두대 사용 X
- L3 두개를 밑으로
- k8s 컨트롤러+ 노드 같이 씀
  - 권장 컨트롤러 3대 + 노드 n 대
  - 보통 동일 스펙
  - 파일서버 (별도 도커가아닌 k8s내에 정의해야함) 네트워크 트래픽
    - qos모듈 사용해야
    - L4만 뺌
  - mongodb(opensource) 비용 운영 어려움 예상 (H.V에서 운영)
    mariaDB 증설관점에서 문제 발생 가능
  - VPN 통해서 접속
- calico qos
  - k8s 안에 컴포넌트: qos제어
  - calico 방식 대신 clusterfs로 따로 빼서 업로드 다운로드
  - 도메인 구매 H.V 소속 도메인 쓸지, 새로 구매할지 미정


- Build Steps 몇개인지 확인 + Dockefile 경로

- VCS root name
https://devportal.kaonrms.com/konnect/vendor/etisalat/etisalat-fe-api.git#refs/heads/etisalat

- Repository URL
https://devportal.kaonrms.com/konnect/vendor/etisalat/etisalat-fe-api.git
docker_rep
kaon.1234

- Default branch:
refs/heads/console


- Branch specification
refs/heads/*

- tags
konnect/vendor/etisalat/etisalat-fe-api
krms3.1-aws-etisalat-stage/back-end/etisalat-fe-api

devportal.kaonrms.com:5050/konnect/cs/krms-mail-sender:%build.counter%.%teamcity.build.branch%.%GitShortHash%
devportal.kaonrms.com:5050/konnect/cs/krms-mail-sender:latest

krms-dev.kaonrms.com:10443/krms3.1-aws-core/cs/krms-mail-sender:%build.counter%.%teamcity.build.branch%.%GitShortHash%
krms-dev.kaonrms.com:10443/krms3.1-aws-core/cs/krms-mail-sender:latest



root
Kaon.wa!!0

xperi-fe-partner-api
etisalat-fe-partner-api


krms3.1-aws-console
krms3.1-aws-core

In istio service mesh implementation, i understood as follows:
1. user request
2. istio Gateway distribute to VirtualService
3. VirtualService sends to DestinationRule

What is IstioOperator and how do i configure it?

088356671508.dkr.ecr.ap-northeast-2.amazonaws.com/krms3.1-aws-console/front-end/fe-web:latest


apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: krms-gateway-core-console-tcp
  namespace: core
spec:
  selector:
    istio: ingressgateway-nlb-stage-console
  servers


git clone https://devportal.kaonrms.com/konnect/service-group/sg-task.git
cd sg-task
git checkout -b console
git pull origin console
git branch

git add .
git commit -m 'Teamcity VCS Trigger test'
git push -u origin console

devportal.kaonrms.com:5050/konnect/sfg/sfg-management:%build.counter%.%teamcity.build.branch%.%GitShortHash%
devportal.kaonrms.com:5050/konnect/sfg/sfg-management:latest

krms-dev.kaonrms.com:10443/krms3.1-aws-core/sfg/sfg-management:%build.counter%.%teamcity.build.branch%.%GitShortHash%
krms-dev.kaonrms.com:10443/krms3.1-aws-core/sfg/sfg-management:latest


krms-dev.kaonrms.com:10443/krms3.1-aws-core/cs/krms-mail-sender:%build.counter%.%teamcity.build.branch%.%GitShortHash%
krms-dev.kaonrms.com:10443/krms3.1-aws-core/cs/krms-mail-sender:latest


+:*
-:onp-*
-:aws-*

-:console
-:experi
-:etisalat


210.95.66.75
sudo du -hc --max-depth=1 .

REMOVE dangling images
docker rmi $(docker images --filter "dangling=true" -q --no-trunc)



https://krms-dev.kaonrms.com/partner-api/v1/docs/index.html
https://krms-dev.kaonrms.com/device-api/v1/docs/index.html


* build/Dockerfile로 빌드시 에러 발생  (go 버전 1.19)

stage-rds-001.cslxnjy41ka6.ap-northeast-2.rds.amazonaws.com
Step 9/16 : RUN go build -v -o sfg-management -buildvcs=false -ldflags "-X 'main.GitCommit=$GIT_SHORT_HASH' -X 'main.BuildTime=`date +%Y/%m/%d/%H:%M`'"

[08:08:08][Step 2/3] go.buf.build/grpc/go/konnect/core/task/root/v1
[08:08:08][Step 2/3] google.golang.org/grpc/reflection
[08:08:08][Step 2/3] go.buf.build/grpc/go/konnect/services/sg/v1
[08:08:08][Step 2/3] go.buf.build/grpc/go/konnect/services/sg/root/v1
[08:08:09][Step 2/3] go.buf.build/grpc/go/konnect/services/sg/event/v1
[08:08:09][Step 2/3] go.buf.build/grpc/go/konnect/services/sfg/management/v1
[08:08:09][Step 2/3] sfg-management/internal/grpc/handler
[08:08:16][Step 2/3] The command '/bin/sh -c go build -v -o sfg-management -buildvcs=false -ldflags "-X 'main.GitCommit=$GIT_SHORT_HASH' -X 'main.BuildTime=`date +%Y/%m/%d/%H:%M`'"' returned a non-zero code: 2
[08:08:16][Step 2/3]
[08:08:16][Step 2/3] Process exited with code 2
[08:08:16][Step 2/3] Process exited with code 2 (Step: Docker build (Docker))
[08:08:16][Step 2/3] Step Docker build (Docker) failed

mkdir 001.console-stage
mkdir 002.xperi-stage
mkdir 003.etisalat-stage



- DB 스키마 분리 (console, etisalat, xperi)
- yaml 파일 (console, etisalat, xperi)

001.df-root         003.df-mtp-xmpp     005.df-mqtt-broker
002.df-cwmp-parser  004.df-cwmp-engine  006.df-api


stage-rds-001.cslxnjy41ka6.ap-northeast-2.rds.amazonaws.com


- mysql source 	125.132.210.135/32

- Etv InBound Rules


- RDS (MariaDB)
  stage-rds-001.cslxnjy41ka6.ap-northeast-2.rds.amazonaws.com:3306
  Engine option: MariaDB
  Identifier: stage-rds-001
  Instance db.m6g.large
  Storage type: General Purpose SSD (gp2)
    
- DocumentDB
  stage-docdb-001

- RabbitMQ
  stage-single-mq-001

- Redis
  Create Security Group
    stage-redis-001
  Create subnet group
    stage-redis-001
  Create Cluster
    stage-redis-001



- is modifiable, value, source
cluster-enabled ->  no yes user
databases -> No 16G


001.service_cm.yaml
  XMPP_DOMAIN
  XMPP_HOST
  DF_API_URL















# Message Queue
MQ_HOST: "b-148c9298-81e1-4317-b107-83ecbde27408.mq.ap-northeast-2.amazonaws.com"
MQ_PORT: "5671"
MQ_USER: "krms"
MQ_PW: "kaon.12345678"

# REDIS AWS - Cluster
REDIS_CLUSTERS: "stage-redis-001.4sbg3f.clustercfg.apn2.cache.amazonaws.com:7480"

# Document DB (master)
DOCDB_USER: "krms"
DOCDB_PW: "kaon.1234"
DOCDB_DBNAME: "krms"
DOCDB_CLUSTERS: "stage-docdb-001.cluster-cslxnjy41ka6.ap-northeast-2.docdb.amazonaws.com:27077"
#readPreference option

# RDB (master)
RDB_TYPE: "mariadb"
RDB_HOST: "stage-rds-001.cslxnjy41ka6.ap-northeast-2.rds.amazonaws.com"
RDB_PORT: "3306"
RDB_USER: "krms"
RDB_PW: "kaon.1234"
RDB_DBNAME: "krms_31"





egrep -R XMPP_DOMAIN *

[ec2-user@ip-172-34-72-189 001.df]$ egrep backing-service -R *
002.df-cwmp-parser/deployment.yaml:              name: backing-services
003.df-mtp-xmpp/backing_service_cm.yaml:  name: backing-services
003.df-mtp-xmpp/deployment.yaml:              name: backing-services
004.df-cwmp-engine/deployment.yaml:              name: backing-services
005.df-mqtt-broker/deployment.yaml:              name: backing-services



002.xperi-stage/001.df/003.df-mtp-xmpp/backing_service_cm.yaml:  XMPP_DOMAIN: "etv-dev-xmpp.krms.kaonmedia.com"
003.etisalat-stage/001.df/003.df-mtp-xmpp/backing_service_cm.yaml:  XMPP_DOMAIN: "etv-dev-xmpp.krms.kaonmedia.com"
004.core/001.df/003.df-mtp-xmpp/backing_service_cm.yaml:  XMPP_DOMAIN: "etv-dev-xmpp.krms.kaonmedia.com"
004.core/001.df/004.df-cwmp-engine/deployment.yaml:          - name: XMPP_DOMAIN
005.backing_service/backup-230531/001.service_cm.yaml:  XMPP_DOMAIN: "etv-dev-xmpp.krms.kaonmedia.com"
005.backing_service/001.service_cm.yaml:  XMPP_DOMAIN: "etv-dev-xmpp.krms.kaonmedia.com"
007.helm-TEST-krms/001.df/004.df-cwmp-engine/backup-230420/deployment.yaml:          - name: XMPP_DOMAIN
007.helm-TEST-krms/001.df/004.df-cwmp-engine/values.yaml:        - name: XMPP_DOMAIN
999.etv/004.core/001.df/004.df-cwmp-engine/deployment.yaml:          - name: XMPP_DOMAIN

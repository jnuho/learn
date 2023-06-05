

- Istio 시스템
  - IngressGateway (각 vendor별로 각각 리스트 형식으로 정의)
    - ALB (NodePort): dashboard, cwmp
    - NLB (LoadBalancer): 

- Ingress

- Core > gateway

- 신규 서비스 추가하기
  - istio: 001.istio.yaml
    - nlb에 추가 : port, targetPort
    - ./istioctl upgrade -f 001.istio.yaml
  - gateway: 001.krms-gateway-core-console-tcp.yaml 수정
    - servers에 리스트추가 (port, host)
  - AWS > Route53  > A 레코드 (vs.yaml 참고)
    - console-mqtt.rmsinfo.net
    - rmsinfo-nlb-stage-console-35a662e3756656e4.elb.ap-northeast-2.amazonaws.com.
  - 쿠버네티스 자원 생성 (deployment, service, vs)
    - df-cwmp-parser는 vs자원 없어서 gw, 



  - console 벤더에 추가 (vs-console.yaml)

telnet console-xmpp.rmsinfo.net 5222
telnet console-mqtt.rmsinfo.net 1883
telnet console-df-root.rmsinfo.net 9000



- 001.df

```
001.df-root         003.df-mtp-xmpp     005.df-mqtt-broker
002.df-cwmp-parser  004.df-cwmp-engine  006.df-api
```


Error [IST0139] (MutatingWebhookConfiguration istio-sidecar-injector ) Webhook overlaps with others: [istio-revision-tag-default/rev.namespace.sidecar-injector.istio.io]. This may cause injection to occur twice.

k delete MutatingWebhookConfiguration -n istio-system

- 005.backing_service


```sh
apk update
apk add mysql-client
mysql -h stage-rds-002.cslxnjy41ka6.ap-northeast-2.rds.amazonaws.com -u krms -pkaon.1234
```

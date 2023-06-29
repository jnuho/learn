

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

- podAntiAffinity

```
Defining `podAntiAffinity` for all 40 microservices might not be necessary or recommended in your scenario. It depends on the specific requirements and characteristics of your microservices and the overall application architecture. Here are some factors to consider:

1. Inter-service communication: If your microservices heavily rely on inter-service communication and data exchange, placing them on separate nodes using `podAntiAffinity` might introduce additional network latency and overhead. In such cases, it might be more efficient to co-locate certain microservices on the same node to minimize network latency.

2. Resource requirements: If your microservices have varying resource requirements, spreading them across different nodes using `podAntiAffinity` can help balance the resource utilization and prevent contention. However, if your nodes have sufficient resources to handle the workload of all microservices, it might not be necessary to enforce strict anti-affinity.

3. Availability and fault tolerance: Consider the desired level of availability and fault tolerance for your application. If running multiple instances of each microservice on different nodes is critical for high availability, then using `podAntiAffinity` can help distribute the workload. However, if the loss of a single node does not significantly impact your application, strict anti-affinity might not be required.

4. Performance and scalability: Enforcing `podAntiAffinity` can distribute the workload across nodes, potentially improving performance and scalability by utilizing the resources of multiple nodes. However, this can also introduce additional overhead in terms of inter-node communication. Evaluate the performance requirements of your microservices and the capacity of your nodes to determine the trade-offs.

In summary, instead of blindly applying `podAntiAffinity` to all microservices, it's important to consider the specific characteristics, requirements, and constraints of your application. Evaluate factors such as inter-service communication, resource requirements, availability needs, and performance considerations to determine the appropriate placement and affinity rules for your microservices. It's also worth considering performance testing and experimentation to find the optimal configuration.
```


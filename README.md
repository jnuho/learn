I created personal notes about various computer science topics.

<br><hr>
### Contents

- [Network basic](#network-basic)
- [Ubuntu network setting](#ubuntu-network-setting)
- [SSL Termination](#ssl-termination)
- [Pod Network](#pod-network)
- [Service Network](#service-network)
- [Ingress Network](#ingress-network)

[↑ top](#contents)
<br><br>

## Network basic

- Private IP addresses are not globally unique and are reserved for internal use only.
  - They are typically used behind a network address translation (NAT) device
  - to allow multiple devices within a network to share a single public IP address.

- IPV4 class
  - 주소를 A,B,C 클래스로 나눔
  - B, C를 주로 사용함. A는 국가단위 방대한 네트워크
  - A: 0....... 8 8 8 = Network bit(7-bit) + Host bit(24-bit)
    - 1개 네트워크가 2^24 개 ip 보유
    - 이런 네트워크가 2^7 개 만큼 있음
    - 1개 네트워크 규모는 크지만 네트워크 개수는 적음
    - Network bit: 0~127
    - Host bit: 0.0.0 ~ 255.255.255
  - B: 10...... 8 8 8 = Network bit(14-bit)+ Host bit(16-bit)
    - 1개 네트워크가 2^16 개 ip 보유
    - 이런 네트워크가 2^14 개 만큼 있음
    - Network bit: 128.0 ~ 191.255
    - Host bit: 0.0 ~ 255.255
  - C: 110..... 8 8 8 = Network bit(21-bit) + Host bit(8-bit)
    - 1개 네트워크가 2^8 개 ip 보유
    - 이런 네트워크가 2^21 개 만큼 있음
    - Network bit: 192.0.0 ~ 223.255.255
    - Host bit: 0 ~ 255

- 서브넷으로 IP대역을 나눌수 있음

- 서브넷 2개

```
# Subnet A
#   211.11.124.0/25
#   시작ip/고정되어있는 앞에 비트개수
211.11.124.0   (...00000000)
211.11.124.127 (...01111111)
-------------
# Subnet B
#   211.11.124.128/25
211.11.124.128 (...10000000)
211.11.124.255 (...11111111)
```

- 서브넷 4개

```
# Subnet A
#   211.11.124.0/26
211.11.124.0   (...00000000)
211.11.124.63 (...00111111)
-------------
# Subnet B
#   211.11.124.64/26
211.11.124.64 (...01000000)
211.11.124.127 (...01111111)
# Subnet C
#   211.11.124.128/26
211.11.124.128 (...10000000)
211.11.124.191 (...10111111)
# Subnet D
#   211.11.124.192/26
211.11.124.192 (...11000000)
211.11.124.255 (...11111111)
```

[↑ top](#contents)
<br><br>

## L4, L7 스위치

- https://itwiki.kr/w/L7_%EC%8A%A4%EC%9C%84%EC%B9%98
- https://driz2le.tistory.com/24?category=563475
- L4: network switch
- L7: ALB. Application Layer

## Ubuntu network setting

Ubuntu server setup

> This is the Unix philosophy: Write programs
> that do one thing and do it well.
>
> *Doug McIlroy*

- [*linux setup*]()


```sh
ifconfig -a
vim /etc/netplan/00-installer-config.yaml

sudo netplan apply
ifconfig -a
```

```yaml
# This is the network config written by 'subiquity'
network:
  version: 2
  renderer: networkd
  ethernets:
    ens160:
      addresses:
      - 172.16.6.76/24
      gateway4: 172.16.6.222
      nameservers:
        addresses:
        - 8.8.8.8
```

[↑ top](#contents)
<br><br>


## SSL Termination

- [*ssl termination*](https://www.f5.com/glossary/ssl-termination)

[↑ top](#contents)
<br><br>


## Pod Network

https://medium.com/google-cloud/understanding-kubernetes-networking-pods-7117dd28727

- Pod ip address is ephemeral.

[↑ top](#contents)
<br><br>

## Service Network

https://medium.com/google-cloud/understanding-kubernetes-networking-services-f0cb48e4cc82

```sh
kubectl apply -f deployment.yaml
kubectl get pods --selector=app=service_test_pod -o jsonpath='{.items[*].status.podIP}'
  10.0.1.2 10.0.2.2
```

```yaml
kind: Deployment
apiVersion: apps/v1
metadata:
  name: service-test
spec:
  replicas: 2
  selector:
    matchLabels:
      app: service_test_pod
  template:
    metadata:
      labels:
        app: service_test_pod
    spec:
      containers:
      - name: simple-http
        image: python:2.7
        imagePullPolicy: IfNotPresent
        command: ["/bin/bash"]
        args: ["-c", "echo \"<p>Hello from $(hostname)</p>\" > index.html; python -m SimpleHTTPServer 8080"]
        ports:
        - name: http
          containerPort: 8080
```

- Access via Pod IP
  - If the pod dies and restarted the ip changes
  - so the service-test-client1 fails to get 200 response since it cannot reach the pod address - 10.0.2.2

```sh
kubectl apply -f service-test-client1.yaml
kubectl logs service-test-client1
  HTTP/1.0 200 OK
  <!-- blah --><p>Hello from service-test-6ffd9ddbbf-kf4j2</p>
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: service-test-client1
spec:
  restartPolicy: Never
  containers:
  - name: test-client1
    image: alpine
    command: ["/bin/sh"]
    args: ["-c", "echo 'GET / HTTP/1.1\r\n\r\n' | nc 10.0.2.2 8080"]
```

- Service definition

```sh
kubectl apply -f service.yaml
```

```yaml
kind: Service
apiVersion: v1
metadata:
  name: service-test
spec:
  selector:
    app: service_test_pod
  ports:
  - port: 80
    targetPort: http
```

- Access via Service name
  - k8s Cluster DNS resolution
  - "service-test" resolves to Service IP
    - responses from both server pods with each getting approximately 50% of the requests

```sh
kubectl apply -f service-test-client2.yaml
kubectl logs service-test-client2
  HTTP/1.0 200 OK
  <!-- blah --><p>Hello from service-test-6ffd9ddbbf-kf4j2</p>

# Service Network
gcloud container clusters describe test | grep servicesIpv4Cidr
  servicesIpv4Cidr: 10.3.240.0/20
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: service-test-client2
spec:
  restartPolicy: Never
  containers:
  - name: test-client2
    image: alpine
    command: ["/bin/sh"]
    args: ["-c", "echo 'GET / HTTP/1.1\r\n\r\n' | nc service-test 80"]
```

- How it works
  - Service Network CIDR differs from that of Pod Network
  - Client make http request using DNS name "service-test"
  - The cluster DNS system resolves that name to the service ClusterIP
  - Network interfaces (veth0-> cbr0, etho0) ) does not understand service ClusterIP,
  - so it forwards it back to the top-level router/gateway and redirected to one of the server pods
  - kube-proxy

- kube-proxy



[↑ top](#contents)
<br><br>

## Ingress Network

https://medium.com/google-cloud/understanding-kubernetes-networking-ingress-1bc341c84078


[↑ top](#contents)
<br><br>



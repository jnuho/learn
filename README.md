I created personal notes about various computer science topics.

<br><hr>
### Contents

- [Network basic](#network-basic)
- [Ubuntu network setting](#ubuntu-network-setting)
- [SSL Termination](#ssl-termination)

[↑ top](#contents)
<br><br>

## Network basic

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

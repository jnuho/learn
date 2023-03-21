`personal notes about various computer science topics`


- [1. 우분투 서버 네트워크 설정](#1-우분투-서버-네트워크-설정)


### 1. 우분투 서버 네트워크 설정

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



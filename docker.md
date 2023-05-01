

- `From Kyobo > 시작하세요! 도커/쿠버네티스'

- 도커 볼륨

```sh
docker run -d \
--name wordpressdb_hostvolume \
-e MYSQL_ROOT_PASSWORD=password \
-e MYSQL_DATABASE=wordpress \
-v /home/wordpress_db:/var/lib/mysql \
mysql:5.7

docker run -d \
-e WORDPRESS_DB_PASSWORD=password \
--name wordpress_hostvolume \
--link wordpressdb_hostvolume:mysql \
-p 80 \
wordpress

# 호스트의 디렉터리를 컨테이너의 디렉터리에 마운트 함 (overwrite)
#   원래 존재하던 디렉터리에 호스트의 볼륨을 공유하면 컨테이너의 디렉터리 자체가 덮어씌워짐
# 호스트에 없다면 컨테이너 디렉터리가 호스트에 복사됨
# (alice106/volume_test 이미지는 /home/testdir_2에 test라는 파일을 가진 이미지임!)
docker run -i -t \
--name volume_override \
-v /home/wordpress_db:/home/testdir_2 \
alice106/volume_test

# 볼륩생성
docker volume create --name myvolume
docker run -i -t --name my_valume_1 \
-v myvolume:/root/ \
ubuntu:14.04
docker inspect --type volume myvolume
```


- 도커 네트워크
  - veth : 컨테이너 시작할때 생성
  - docker0 : 브리지 네트워크. 호스트의 eth0 인터페이스와 이어주며, 외부와 통신할 수 있는 환경 제공
  - eth0 인터페이스는 호스트의 veth 인터페이스와 연결됐으며, veth 인터페이스는 docker0 브리지와 바인딩돼 외부와 통신 할 수 있음.

- 도커 네트워크 기능
  - bridge
  - host
  - none
  - container


```sh
docker network ls
docker network inspect bridge

# bridge
docker network create --driver bridge mybridge
docker run -it --name mynetwork_container \
--net mybridge \
ubuntu:14.04

docker network create --driver=bridge \
--subnet=172.72.0.0/16 \
--ip-range=172.72.0.0/24 \
--gateway=172.72.0.1 \
my_custom_network

# host
#  호스트 네트워크 환경을 그대로 쓸 수 있음
#  별도의 포트포워딩 없이 바로 서비스 가능
docker run -it --name network_host \
--net host \
ubuntu:14.04

# none
#  아무런 네트워크를 쓰지않음
docker run -it --name network_none \
--net none \
ubuntu:14.04

# container
#  다른 컨테이너의 네트워크 네임스페이스 환경 공유 : 내부ip, mac address
#  두 컨테이너의 etho0에 대한 정보가 완전히 같음
docker run -it -d --name network_container_1 ubuntu:14.04
docker run -it -d --name network_container_2 \
--net container:network_container_1 \
ubuntu:14.04
```

- 브리지 네트워크와 --net-alias
  - 특정 호스트 이름으로 컨테이너 여러 개에 접근 가능

```sh
docker network create --driver bridge mybridge

docker run -it -d --name network_alias_container1 \
--net mybridge \
--net-alias alicek106 \
ubuntu:14.04

docker run -it -d --name network_alias_container2 \
--net mybridge \
--net-alias alicek106 \
ubuntu:14.04

docker run -it -d --name network_alias_container3 \
--net mybridge \
--net-alias alicek106 \
ubuntu:14.04


# 3개의 컨테이너에 접근할 컨테이너 생성뒤 alicek106이라는 호스트이름으로 ping 요청
# 라운드 로빈 방식으로 3개 ip가 번갈아 통신
docker run -it --name network_alias_ping \
--net mybridge \
ubuntu:14.04

  ping -c 1 alicek106
  ping -c 1 alicek106
  ping -c 1 alicek106

  apt update
  apt install dsnutils
  dig alicek106
      alicek106.    600   IN  A   172.18.0.5
      alicek106.    600   IN  A   172.18.0.3
      alicek106.    600   IN  A   172.18.0.4
```

- MacVLAN 네트워크


- 컨테이너 로깅



```sh
docker logs --tail 2 mysql
docker logs --since 1474765979 mysql
docker logs -f -t mysql

docker run -it \
--log-opt max-size=10k --log-opt max-file=3 \
--name log-test ubuntu:14.04
```


- fluentd 로깅
  - 각종 로그를 수집하고 저장할 수 있는 기능 제공하는 오픈소스 도구

- AWS Cloudwatch log




- 컨테이너 메모리 제한

- 컨테이너 CPU 제한

- Block I/O 제한


- 스토리지 드라이버와 컨테이너 저장 공간 제한


- 도커 이미지


- 도커 사설 레지스트리
  - 사설 레지스트리 컨테이너 생성

```sh
docker run -d --name myregistry \
-p 5000:5000 \
--restart=always \
registry:2.6
```

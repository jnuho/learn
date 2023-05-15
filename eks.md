
https://medium.com/avmconsulting-blog/deploying-a-kubernetes-cluster-with-amazon-eks-9455e7e7828


### IAM Role

- IAM > Roles > Create Roles
  - Policies: AmazonEKSClusterPolicy, AmazonEKSServicePolicy

### VPC

- Create VPC using Cloudformation.
  - 2개 이상의 subnet이 필요하며, 외부 서비스를 고려해야하기 때문에 반드시 public subnet, private subnet 각각이 필요합니다.
  - 작업자 노드가 클러스터에 등록하기 위해 VPC 설정 확인
    - DNS resolution Enabled 확인하기
    - DNS hostnames Enabled 확인하기
  

```yaml
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock:  !Ref VpcBlock
      EnableDnsSupport: true
      EnableDnsHostnames: true
      Tags:
      - Key: Name
        Value: !Sub '${AWS::StackName}-VPC'
```


- ClusterName: testcluster-001
- CloudFormation Stack : testcluster-001-Stack-VPC-Private-Public
  - VpcBlock
    - CIDR: 172.32.0.0/16
  - PublicSubnet01Block
    - CIDR: 172.32.0.0/18
    - 00000000 (0)  - 00111111 (63)
  - PublicSubnet02Block
    - CIDR: 172.32.64.0/18
    - 01000000 (64) - 01111111 (127)
  - PrivateSubnet01Block
    - CIDE: 172.32.128.0/18
    - 10000000 (128) - 10100000 (191)
  - PrivateSubnet02Block
    - CIDR: 172.32.192.0/18
    - 11000000 (192) - 11111111 (255)

### 쿠버네티스 클라이언트 설치

- EKS 클러스터에 IAM 권한을 부여하기 위해서는 kubelet, kubectl, heptio이 필요
  - eksctl 또는 kubectl 사용가능

- kubectl 설치

```sh
curl -o kubectl https://amazon-eks.s3-us-west-2.amazonaws.com/1.10.3/2018-06-05/bin/linux/amd64/kubectl
chmod +x ./kubectl
mkdir bin
cp ./kubectl $HOME/bin/kubectl
export PATH=$HOME/bin:$PATH
echo 'export PATH=$HOME/bin:$PATH' >> ~/.bashrc
kubectl version --short --client
```

- aws-iam-authenticator 설치

```sh
curl -Lo heptio-authenticator-aws https://github.com/kubernetes-sigs/aws-iam-authenticator/releases/download/v0.5.9/aws-iam-authenticator_0.5.9_linux_amd64
chmod +x ./heptio-authenticator-aws
cp ./heptio-authenticator-aws $HOME/bin/heptio-authenticator-aws && export PATH=$HOME/bin:$PATH
echo 'export PATH=$HOME/bin:$PATH' >> ~/.bashrc
```

### EKS 구성

- EKS는구축하기 위해서 EKS클러스터생성과 노드그룹을 생성해야 합니다.

### kubectl 수정

- 위에서 생성한 EKS에 연결
  - server: <endpoint-url>
  - certificate-authority-data: "<base64-encoded-ca-cert>"
  - "<cluster-name>"

```sh
mkdir -p ~/.kube
cd .kube
export KUBECONFIG=$KUBECONFIG:~/.kube/config-devopsadvocate
echo 'export KUBECONFIG=$KUBECONFIG:~/.kube/config-devopsadvocate' >> ~/.bashrc
kubectl get svc

cat > config-devopsadvocate

apiVersion: v1
clusters:
- cluster:
    server: <endpoint-url>
    certificate-authority-data: "<base64-encoded-ca-cert>"
  name: kubernetes
contexts:
- context:
    cluster: kubernetes
    user: aws
  name: aws
current-context: aws
kind: Config
preferences: {}
users:
- name: aws
  user:
    exec:
      apiVersion: client.authentication.k8s.io/v1alpha1
      command: heptio-authenticator-aws
      args:
        - "token"
        - "-i"
        - "<cluster-name>"
        # - "-r"
        # - ""
```

1. aws cli

```sh
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

2. kubectl

```sh
curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.26.2/2023-03-17/bin/darwin/amd64/kubectl
chmod +x ./kubectl
mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$HOME/bin:$PATH
kubectl version --short --client
```

3. eksctl

```sh
# for ARM systems, set ARCH to: `arm64`, `armv6` or `armv7`
ARCH=amd64
PLATFORM=$(uname -s)_$ARCH

curl -sLO "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$PLATFORM.tar.gz"

tar -xzf eksctl_$PLATFORM.tar.gz -C /tmp && rm eksctl_$PLATFORM.tar.gz

sudo mv /tmp/eksctl /usr/local/bin

eksctl version
```

4. Create Cluster



```sh
eksctl create cluster --name testcluster-001 --region region-code
```



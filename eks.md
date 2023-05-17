
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


- ClusterName: krms31-stage
- CloudFormation Stack : krms31-stage-Stack-VPC-Public Only

```
AWSTemplateFormatVersion: '2010-09-09'
Description: 'Amazon EKS Sample VPC - Public subnets only'
Parameters:
  VpcBlock:
    Type: String
    Default: 192.168.0.0/16
    Description: The CIDR range for the VPC. This should be a valid private (RFC 1918) CIDR range.
  Subnet01Block:
    Type: String
    Default: 192.168.64.0/18
    Description: CidrBlock for subnet 01 within the VPC
  Subnet02Block:
    Type: String
    Default: 192.168.128.0/18
    Description: CidrBlock for subnet 02 within the VPC
  Subnet03Block:
    Type: String
    Default: 192.168.192.0/18
    Description: CidrBlock for subnet 03 within the VPC. This is used only if the region has more than 2 AZs.
```
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
curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.26.2/2023-03-17/bin/linux/amd64/kubectl
chmod +x ./kubectl
mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$HOME/bin:$PATH
kubectl version --short --client
```

3. kubectl-configure EKS cluster

```sh
aws eks update-kubeconfig --region ap-northeast-2 --name testcluster-001
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

- AWS Console > Create cluster
- Create an IAM OpenID Connect (OIDC) provider
- Configure your cluster for the Amazon VPC CNI plugin for Kubernetes plugin before deploying Amazon EC2 nodes to your cluster. By default, the plugin was installed with your cluster. When you add Amazon EC2 nodes to your cluster, the plugin is automatically deployed to each Amazon EC2 node that you add

```sh
eksctl create cluster --name krms31-stage --region region-code
```

5. vpc-cni

- NOTE: aws-node 서비스어카운트는 cluster 생성시 있음
- role생성 -> policy attach-> annotate serviceaccount 하면 VPC-CNI Add-on에 IAM role 추가됨
- Annotates the existing aws-node Kubernetes service account with the ARN of the IAM role that is created.
- Create Node IAM Role

```sh
cat > node-role-trust-relationship.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF

aws iam create-role \
  --role-name testcluster-001-AmazonEKSNodeRole \
  --assume-role-policy-document file://"node-role-trust-relationship.json"

aws iam attach-role-policy \
  --policy-arn arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy \
  --role-name testcluster-001-AmazonEKSNodeRole
aws iam attach-role-policy \
  --policy-arn arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly \
  --role-name testcluster-001-AmazonEKSNodeRole

aws iam attach-role-policy \
  --policy-arn arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy \
  --role-name testcluster-001-AmazonEKSNodeRole
```

- Create Node Group
  - select IAM Role

```sh
aws eks describe-cluster --name testcluster-001 --query "cluster.identity.oidc.issuer" --output text
```

6. Create Node IAM Role

- https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html

```sh
aws iam create-role \
  --role-name krms31-stage-AmazonEKSNodeRole \
  --assume-role-policy-document file://"node-role-trust-relationship.json"

aws iam attach-role-policy \
  --policy-arn arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy \
  --role-name krms31-stage-AmazonEKSNodeRole

aws iam attach-role-policy \
  --policy-arn arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly \
  --role-name krms31-stage-AmazonEKSNodeRole
```

7. Create Node Group

- Choose Name
- Create Node IAM Role
- Security Group?






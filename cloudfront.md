

- Revision: 2023-03-21 junho


### CloudFront 서비스

- [Reference](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-overview.html)

CloudFront는 low-latency cdn으로 빠른 컨텐츠 제공 뿐 아니라, Access control을 통해 secure한 컨텐츠를 제공하는 서비스이다. 컨텐츠 제공 회사는 S3 업로드 컨텐츠들의 origin server(AWS S3, HTTP server)를 통한 접근을 제한하고자 한다.

S3 버킷에 업로드시 해당 객체에 대한 object url이 생성되는데,
CloudFront를 통해 이 origin url에 대한 접근을 제한할 수 있으며, 다음 2가지 방법이 있다:

1. S3가 아닌 CloudFront Url을 통한 컨텐츠 접근 하도록 제한
	- S3생성
	- CloudFront OAC (Origin Access Control) 생성
	- 해당 policy -> S3 policy에 추가


2. CloudFront signed url 또는 signed cookies를 통해 컨텐츠 접근하도록 제한
	- CloudFront 설정하기
	- Signed URL 생성하여 인증된 사용자에게 제공 하거나, 'Set-Cookie' 헤더를 보내서 인증된 사용자를 위한 signed cookies 설정하기

- [Create a key pair for a trusted key group (recommended)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-trusted-signers.html#private-content-creating-cloudfront-key-pairs) for the Signer


- To create a key pair
	- The signer uses its private key to sign the URL or cookies,
	- CloudFront uses the public key to verify the signature.

```sh
openssl genrsa -out private_key.pem 2048
openssl rsa -pubout -in private_key.pem -out public_key.pem
cat public_key.pem
```

- To upload the public key to CloudFront
	- CloudFront > Public Key
	- `Public ID` generated -> used to sign url using Go Sdk (as 'keyID')

- To add the public key to a key group
	- Add key group > select public key


- [Go sdk](https://docs.aws.amazon.com/sdk-for-go/api/service/cloudfront/sign/) 사용하여 url sign하기 (위에서 생성한 private key로 서명)


```go
package main

import (
	"fmt"
	"log"
	"time"
  "github.com/aws/aws-sdk-go/service/cloudfront/sign"
)

func main() {

  // Using the Amazon CloudFront default Canned Policy.
  // cat public_key.pem
  keyID := "KLYEEKTJFHDEH"
  privKey, err := sign.LoadPEMPrivKeyFile("./private_key.pem")
	rawURL := "https://d1q4vfk7jj7pb1.cloudfront.net/test.txt"
  if err != nil {
    log.Fatalf("Failed to Load PEM private_key file, err: %s\n", err.Error())
  }

  // Sign URL to be valid for 1 hour from now.
	// using canned policy
  signer := sign.NewURLSigner(keyID, privKey)
  signedURL, err2 := signer.Sign(rawURL, time.Now().Add(1*time.Hour))
  if err2 != nil {
      log.Fatalf("Failed to sign url, err: %s\n", err2.Error())
  }
	fmt.Println(signedURL);
}
```



### CloudFront Route53에 연결하기

- Route 53 > Hosted zones > Create record
	- N. Virginia 에서만 추가 가능. 관련 메시지:

```
An alias to a CloudFront distribution and another record
in the same hosted zone are global and available only in US East (N. Virginia)
```



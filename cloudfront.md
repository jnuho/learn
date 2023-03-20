
- [doc](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-overview.html)

### CloudFront

CloudFront는 low-latency cdn으로 빠른 컨텐츠 제공 뿐 아니라, Access control을 통해 secure한 컨텐츠를 제공하는 서비스이다.

컨텐츠 제공 회사는 서비스를 구매한 고객을 대상으로 서비스 하기 때문에,
origin server(AWS S3, HTTP server)를 통한 컨텐츠 접근을 제한하길 원한다.
S3 버킷에 contents를 업로드하면 해당 객체에 대한 object url이 생성되며,
CloudFront를 통해 이 origin url에 대한 접근을 제한할 수 있으며, 다음 2가지 방법이 있다:

1. S3가 아닌 CloudFront Url을 통한 컨텐츠 접근 하도록 제한
  origin server; S3 or HTTP server 통한 컨텐츠 접근 제한

- S3생성
- CloudFront OAC(Origin Access Control) 생성
- 해당 policy-> S3 policy에 추가


2. CloudFront signed url 또는 signed cookies를 통해 컨텐츠 접근하도록 제한

- CloudFront 설정하기
- Signed URL 생성하여 인증된 사용자에게 제공 하거나, 'Set-Cookie' 헤더를 보내서 인증된 사용자를 위한 signed cookies 설정하기

- [Go sdk](https://docs.aws.amazon.com/sdk-for-go/api/service/cloudfront/sign/) 적용

- [Create key pairs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-trusted-signers.html#private-content-creating-cloudfront-key-pairs) for the Signer


```go
package main

import (
  "github.com/aws/aws-sdk-go/service/cloudfront/sign"
)

func main() {
  // Using the Amazon CloudFront default Canned Policy.
  // cat public_key.pem
  keyID := ""
  privKey, err := LoadPEMPrivKeyFile("private_key.pem")

  // Sign URL to be valid for 1 hour from now.
  signer := sign.NewURLSigner(keyID, privKey)
  signedURL, err := signer.Sign(rawURL, time.Now().Add(1*time.Hour))
  if err != nil {
      log.Fatalf("Failed to sign url, err: %s\n", err.Error())
  }
}
```




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
  keyID := "public_key"
  // Load the private key from file
  privKey, err := sign.LoadPEMPrivKeyFile("./private_key.pem")
	if err != nil {
    log.Fatalf("Failed to Load PEM private_key file, err: %s\n", err.Error())
  }

	rawURL := "https://d1q4vfk7jj7pb1.cloudfront.net/test.txt"
  // Sign URL to be valid for 1 hour from now.
  signer := sign.NewURLSigner(keyID, privKey)
  signedURL, err2 := signer.Sign(rawURL, time.Now().Add(1*time.Hour))
  if err2 != nil {
      log.Fatalf("Failed to sign url, err: %s\n", err2.Error())
  }
	fmt.Println(signedURL);

}

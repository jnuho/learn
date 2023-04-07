


- krview-dev.kaonrms.net
  - route53 > A Record
    - 13.209.222.91
    - 43.200.10.223
  - Need Health Check to enable DNS Failover
    - Configure DNS Failover:
      - https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring.html



- Health Check

```
Route 53 to check the health of those servers and to respond to DNS queries
for example.com using only the servers that are currently healthy.
```
- Create a record and a Health Check for each resource

```
If you're routing traffic to resources
that you can't create alias records for, such as EC2 instances,
you create a record and a health check for each resource.

```



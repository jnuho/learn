* Istio provides

- Secure
- Connect
- Observe
- Control

Istio injects proxies which runs as containers next to each container inside the pod.
Proxy intercepts service request, apply policys, and route traffic to proxy in another pod.
Proxy receives the request and forward it to the serivce pod container.

* Components:
- Gally receive yaml and validate.
- Pilot convert that confi to envoy configuration and distribute to each proxy
- Policy
- Telemetry
- Citadel : strong identity, certificate to each proxy

* Istio Resources
- Gateway: Works as a Load Balancer that sits on the edge of the istio service mesh. Accepts incoming and outgoing http, tcp connections.
- Virtual Service: Direct traffic between gateway and service or between services.
- Destination Rules: Apply rules (tls, circuit breaking) to the traffic.


* 'istiod' converts hivel level routing rules into Envoy-specific configurations.
  Istiod configurations is propagted into Proxy sidecars
  Proxies can communicate without connecting to istiod control plane
  Internal registry for services and their endpoints.
  Security - works as CA: certificate management
  Metrics and Tracing support


- Istio Ingress Gateway
  - entry point for your cluster
  - alternative to nginx ingress controller
  - runs as a pod and load balances
  - gateway directs traffic to MS using Virtual Service
  - Gateway CRD using yaml

- Istio traffic flow
  - User Request to Istio Gateway (entry point)
    - Evaluate virtual service rules -> forward to MS
    - Envoy proxy inside pod gets the traffic and forward to MS container
  - MS request to another MS
    - MS container to Envoy proxy
    - Envoy proxy apply Virtual service and Destination rules
    - Communite with other Envoy proxy using mTLS (Mutual TLS)
  - Proxy gathers metrics and tracing information about the request and send back to control plane, enabling monitoring of the application




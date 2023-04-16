I created personal notes about various computer science topics.

<br><hr>
### Contents

- [Ubuntu network setting](#ubuntu-network-setting)

[↑ top](#contents)
<br><br>


## Ubuntu network setting

Ubuntu server setup

> This is the Unix philosophy: Write programs
> that do one thing and do it well.
>
> *Doug McIlroy*

- [*linux setup*](https://github.com/gyuho/learn/tree/master/doc/linux_setup)


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


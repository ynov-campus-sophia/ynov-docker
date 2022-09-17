# PART1 docker

# prerequisites

[docker](https://docs.docker.com/engine/install/ubuntu/)
[docker-compose](https://docs.docker.com/compose/install/)

# how to use volumes

# how to use networks

# sha vs tag

# user id

# 2 stages build

# base SO Alpine vs ubuntu

# ENTRYPOINT and CMD

# docker registry and image inspect

# BUILDKIT

# deploy via github actions

# docker basic commands / ps / logs / ls /inspect / exec / run

# basic orchestration via depends_on

```
docker build . -t myimage -f docker/datacollect/Dockerfile
```

# manual build via docker compose

``` 
docker-compose build
```

# manual deploy

``` 
docker-compose push
```

# run datacollect

``` 
docker-compose up -d
```

# stop datacollect

``` 
docker-compose down --remove-orphans
```

# PART2 CI/CD

- Terminology: build, package manager, deploy, package, release, deploy environments, QA, Agile, Sprint Planning

- Topology of IT ecosystem
- INFRASTRUCTURE, SRE, Devops, Dev, Project Management
- KPIs to improve productivity

- orchestration
- CLOUD PROVIDERS

- GITOPS philosophy Argocd / FluxCD

- continuous deployment
- continuous delivery
- continuous integration

- package, test, deploy, monitoring

# PART3 K8s

- Local dev setup (minikube / microk8s)
- deployment / svc / ingress

# PART4 cloud

- digitalocean :

```
kubectl expose deployment hello-world-deployment --type=LoadBalancer --port=80 --target-port=5000 -n inov
```

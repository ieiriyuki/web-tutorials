# Envoy

try rate limit

## quick start

https://www.envoyproxy.io/docs/envoy/latest/start/quick-start/

```
docker run --rm -it -p 9901:9901 -p 10000:10000 envoyproxy/envoy:v1.28-latest

docker run --rm -it \
    -p 9903:9903 \
    -p 10000:10000 \
    -v `pwd`/envoy-override.yaml:/opt/envoy-override.yaml \
    envoyproxy/envoy:v1.28-latest \
    -c /etc/envoy/envoy.yaml \
    --config-yaml "$(cat envoy-override.yaml)"

docker run --rm -it \
    -p 9902:9902 \
    -p 10000:10000 \
    -v `pwd`/envoy-override.yaml:/opt/envoy-override.yaml \
    envoyproxy/envoy:v1.28-latest \
    --mode validate \
    -c /etc/envoy/envoy.yaml \
    --config-yaml "$(cat envoy-override.yaml)"
```

## local rate limit

https://www.envoyproxy.io/docs/envoy/latest/start/sandboxes/local_ratelimit

- `git clone git@github.com:envoyproxy/envoy`

## global rate limit

https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/other_features/global_rate_limiting

- `git clone https://github.com/envoyproxy/ratelimit.git`
- `docker-compose -f docker-compose-example.yml --profile xds-config up --build --remove-orphans`
- `curl -v localhost:8888/header -H "foo: foo"`: 何回かリクエストしていると 429 が返ってくる

```bash
$ curl -v localhost:8888/header -H "foo: foo"

*   Trying 127.0.0.1:8888...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 8888 (#0)
> GET /header HTTP/1.1
> Host: localhost:8888
> User-Agent: curl/7.68.0
> Accept: */*
> foo: foo
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 429 Too Many Requests
< x-envoy-ratelimited: true
< x-ratelimit-limit: 2, 2;w=60
< x-ratelimit-remaining: 0
< x-ratelimit-reset: 4
< date: Wed, 27 Dec 2023 06:30:56 GMT
< server: envoy
< content-length: 0
<
* Connection #0 to host localhost left intact
```

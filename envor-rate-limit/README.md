# Envoy

try rate limit

## quick start

https://www.envoyproxy.io/docs/envoy/latest/start/quick-start/

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

## local rate limit

https://www.envoyproxy.io/docs/envoy/latest/start/sandboxes/local_ratelimit

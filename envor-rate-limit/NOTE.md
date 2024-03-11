`entrypoint.sh`

```bash
#!/usr/bin/env sh
set -e

loglevel="${loglevel:-}"
USERID=$(id -u)


# if the first argument look like a parameter (i.e. start with '-'), run Envoy
if [ "${1#-}" != "$1" ]; then
    set -- envoy "$@"
fi

if [ "$1" = 'envoy' ]; then
    # set the log level if the $loglevel variable is set
    if [ -n "$loglevel" ]; then
        set -- "$@" --log-level "$loglevel"
    fi
fi

if [ "$ENVOY_UID" != "0" ] && [ "$USERID" = 0 ]; then
    if [ -n "$ENVOY_UID" ]; then
        usermod -u "$ENVOY_UID" envoy
    fi
    if [ -n "$ENVOY_GID" ]; then
        groupmod -g "$ENVOY_GID" envoy
    fi
    # Ensure the envoy user is able to write to container logs
    chown envoy:envoy /dev/stdout /dev/stderr
    exec su-exec envoy "${@}"
else
    exec "${@}"
fi
```

`/etc/envoy/envoy.yaml`

```yaml
admin:
  address:
    socket_address:
      protocol: TCP
      address: 0.0.0.0
      port_value: 9901
static_resources:
  listeners:
  - name: listener_0
    address:
      socket_address:
        protocol: TCP
        address: 0.0.0.0
        port_value: 10000
    filter_chains:
    - filters:
      - name: envoy.filters.network.http_connection_manager
        typed_config:
          "@type": type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager
          scheme_header_transformation:
            scheme_to_overwrite: https
          stat_prefix: ingress_http
          route_config:
            name: local_route
            virtual_hosts:
            - name: local_service
              domains: ["*"]
              routes:
              - match:
                  prefix: "/"
                route:
                  host_rewrite_literal: www.envoyproxy.io
                  cluster: service_envoyproxy_io
          http_filters:
          - name: envoy.filters.http.router
            typed_config:
              "@type": type.googleapis.com/envoy.extensions.filters.http.router.v3.Router
  clusters:
  - name: service_envoyproxy_io
    connect_timeout: 30s
    type: LOGICAL_DNS
    # Comment out the following line to test on v6 networks
    dns_lookup_family: V4_ONLY
    lb_policy: ROUND_ROBIN
    load_assignment:
      cluster_name: service_envoyproxy_io
      endpoints:
      - lb_endpoints:
        - endpoint:
            address:
              socket_address:
                address: www.envoyproxy.io
                port_value: 443
    transport_socket:
      name: envoy.transport_sockets.tls
      typed_config:
        "@type": type.googleapis.com/envoy.extensions.transport_sockets.tls.v3.UpstreamTlsContext
        sni: www.envoyproxy.io
```

#!/bin/sh

socat TCP-LISTEN:80,bind=127.0.0.1,fork TCP:nginx-proxy-manager:80 &
socat TCP-LISTEN:81,bind=127.0.0.1,fork TCP:nginx-proxy-manager:81 &
socat TCP-LISTEN:443,bind=127.0.0.1,fork TCP:nginx-proxy-manager:443 &
#socat TCP-LISTEN:53,bind=127.0.0.1,fork TCP:unbound:53 &
#socat UDP-LISTEN:53,bind=127.0.0.1,fork UDP:unbound:53 &

[ -n "$TS_AUTHKEY_FILE" ] && export TS_AUTHKEY="$(cat "$TS_AUTHKEY_FILE")"

/usr/local/bin/containerboot
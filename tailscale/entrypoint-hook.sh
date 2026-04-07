#!/bin/sh

socat TCP-LISTEN:80,bind=127.0.0.1,fork "TCP:${APP_NAME_HOST}_traefik:80" &
socat TCP-LISTEN:443,bind=127.0.0.1,fork "TCP:${APP_NAME_HOST}_traefik:443" &
socat UDP-LISTEN:8189,bind=127.0.0.1,fork "UDP:${APP_NAME_HOST}_traefik:8189" &

[ -n "$TS_AUTHKEY_FILE" ] && export TS_AUTHKEY="$(cat "$TS_AUTHKEY_FILE")"

/usr/local/bin/containerboot
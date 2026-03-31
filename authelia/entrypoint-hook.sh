#!/bin/sh

if [ ! -d "/secrets" ]; then
    mkdir -p /secrets
fi
if [ ! -f "/secrets/jwt" ]; then
    head -c 64 /dev/urandom | base64 > /secrets/jwt
fi
if [ ! -f "/secrets/session" ]; then
    head -c 64 /dev/urandom | base64 > /secrets/session
fi
if [ ! -f "/secrets/storage_key" ]; then
    head -c 64 /dev/urandom | base64 > /secrets/storage_key
fi

export LLDAP_LDAP_BASE_DN="$(echo "$APP_HOST" | sed 's/\./,DC=/g' | sed 's/^/DC=/')"

exec "$@"
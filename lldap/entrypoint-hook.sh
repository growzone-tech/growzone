#!/bin/sh

export LLDAP_LDAP_BASE_DN="$(echo "$APP_HOST" | sed 's/\./,dc=/g' | sed 's/^/dc=/')"

/bootstrap/bootstrap.sh &

exec "$@"
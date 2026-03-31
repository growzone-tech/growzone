#!/usr/bin/env bash

set -e
set -o pipefail

[ -f "/data/.bootstrapped" ] && exit 0

tmpBootstrapDir="$(mktemp -d)"
trap 'rm -rf "$tmpBootstrapDir"' EXIT

export LLDAP_URL="http://localhost:17170"
export LLDAP_ADMIN_USERNAME="$LLDAP_LDAP_USER_DN"
export LLDAP_ADMIN_PASSWORD="$(cat "/run/secrets/LLDAP_ADMIN_PASSWORD")"
export USER_CONFIGS_DIR="$tmpBootstrapDir/user-configs"
export GROUP_CONFIGS_DIR="$tmpBootstrapDir/group-configs"
export USER_SCHEMAS_DIR="$tmpBootstrapDir/user-schemas"
export GROUP_SCHEMAS_DIR="$tmpBootstrapDir/group-schemas"
export DO_CLEANUP="false"

(
    cd "/bootstrap"
    find user-configs group-configs user-schemas group-schemas -type d -exec mkdir -p "$tmpBootstrapDir/{}" \;
    find user-configs group-configs user-schemas group-schemas -type f -exec sh -c 'envsubst < "$1" > "$2/$1"' _ {} "$tmpBootstrapDir" \;
)

/app/bootstrap.sh
touch "/data/.bootstrapped"
exit 0
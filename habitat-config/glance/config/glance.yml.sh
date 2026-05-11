#!/usr/bin/env bash

set -euo pipefail

TARGET_FILE="$1"
TARGET_FILE_CONTENT="$(cat "$TARGET_FILE")"


# ### Init

SOURCE_FILE_DEV_REPOSITORIES="$(mktemp)"
SOURCE_FILE_DEV_GROUPS="$(mktemp)"

DEV_PAGE_NAME="Development"

cat >"$SOURCE_FILE_DEV_REPOSITORIES" <<'EOF'
- growzone-tech/growzone
EOF

cat >"$SOURCE_FILE_DEV_GROUPS" <<'EOF'
- type: html
  title: 'Camera (Outside)'
  source: |
    <div class="glance-lib"
      data-lib-liod
      data-lib-liod-src="https://mediamtx-webrtc.${APP_HOST}/cam0"
      data-lib-liod-classes="aspect-ratio-16-9"
    ></div>
- type: html
  title: 'Camera (Inside 1)'
  source: |
    <div class="glance-lib"
      data-lib-liod
      data-lib-liod-src="https://mediamtx-webrtc.${APP_HOST}/cam1"
      data-lib-liod-classes="aspect-ratio-16-9"
    ></div>
- type: html
  title: 'Camera (Inside 2)'
  source: |
    <div class="glance-lib"
      data-lib-liod
      data-lib-liod-src="https://mediamtx-webrtc.${APP_HOST}/cam2"
      data-lib-liod-classes="aspect-ratio-16-9"
    ></div>
EOF


# ### Add to "Development" page

YQ_ADD_REPOSITORIES='
  (
    .pages[] | select(.name == "'"$DEV_PAGE_NAME"'").columns[0].widgets[] |
    select(.type == "releases") | .repositories
  ) += load("'"$SOURCE_FILE_DEV_REPOSITORIES"'")
'
YQ_ADD_CENTRAL_GROUP='
  (
    .pages[] | select(.name == "'"$DEV_PAGE_NAME"'") |
    .columns[] | select(.size == "full") |
    .widgets[] | select(.type == "group") |
    .widgets
  ) += load("'"$SOURCE_FILE_DEV_GROUPS"'")
'

# shellcheck disable=2016 # Variables are internal to yq expression
TARGET_FILE_CONTENT="$(yq eval "$YQ_ADD_REPOSITORIES" <<<"$TARGET_FILE_CONTENT")"

# shellcheck disable=2016 # Variables are internal to yq expression
TARGET_FILE_CONTENT="$(yq eval "$YQ_ADD_CENTRAL_GROUP" <<<"$TARGET_FILE_CONTENT")"


# ### Clean Up, Print Result and Exit
rm "$SOURCE_FILE_DEV_REPOSITORIES" "$SOURCE_FILE_DEV_GROUPS"

echo "$TARGET_FILE_CONTENT"
exit 0
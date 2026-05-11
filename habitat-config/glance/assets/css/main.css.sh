#!/usr/bin/env bash

set -euo pipefail

cat "$1" | sed -E 's,"/assets/logo/logo_(white|black)\.svg","/assets/logo/logo_color\.svg",g'
exit 0
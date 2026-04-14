[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue?style=flat)](./LICENSE)
![Development: Prototyping](https://img.shields.io/badge/Development-Prototyping-orange?style=flat)
![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-yellow?style=flat)

# Growzone

**🚧
This project is currently under heavy development, any information may be subject to change.
🚧**

A Docker stack designed to transform your grow tent into a fully autonomous, data-driven ecosystem. \
Merge your own needs with those of your plants and help them become the best version of themselves!

## Our Principles

 - **Total Autonomy** \
 Set your plant type and preferred restraints and let the software figure out the rest
 - **Privacy-First** \
 Local data storage by default, encrypted remote access. Your data belongs to you and nobody else
 - **Opinionated Infrastructure** \
 A pre-configured docker stack allowing for quick, painless setup of new devices or resetting existing devices

## Features
 - **Portal** \
 Simple but elegant Glance-powered dashboard with the most important links and information
 - **Live Video Feeds** \
 Integration of attached cameras via MediaMTX
 - **Extensive Monitoring** \
 Visualization of all sensor and actor values as well as microcontroller metrics in pre-configured Grafana Dashboards
 - **Remote Access** \
 Double secured remote access via Tailscale and Authelia
 - **Local Single Sign-On** \
 Log in once to access all available apps according to the users permissions
 - **User Management** \
 Add additional users and assign access permissions via LLDAP

### Planned
 - **Dynamic Climate Control** \
 Automatic adjustment of light, fans and water based on real-time sensor-data analysis
 - **Historical Analytics** \
 Long-term data retention to track growth cycles
 - **Fine-Grained Access Control** \
 Control access to services via LLDAP group assignments
 - **Operation without Tailscale** \
 Purely local operation of the device bypassing the need for Tailscale
 - **Mirroring data to external datasources** \
 Sending device metrics and sensor data to external datasources
 - **Extended Configuration** \
 E.g. defining custom video sources, Tailscale control server, etc.
 - **Configuration Interfaces** \
 Configuration of plant growth schedules and restrictions via API and UI
 - **Domainless Operation**
 Support for other domain providers and domainless operation
 - **And more...**

## Stack & Tools

**User Interface & Management** \
[![Glance](https://img.shields.io/badge/Glance-_?style=flat&logo=glance&logoColor=D9C38C&logoSize=auto&color=gray&labelColor=gray)](https://github.com/glanceapp/glance)
[![LLDAP](https://img.shields.io/badge/LLDAP-_?style=flat&logo=&logoColor=3950A7&logoSize=auto&color=gray&labelColor=gray)](https://github.com/lldap/lldap)

**Networking & Security** \
[![Tailscale](https://img.shields.io/badge/Tailscale-_?style=flat&logo=tailscale&logoColor=242424&logoSize=auto&color=gray&labelColor=gray)](https://tailscale.com/)
[![Traefik](https://img.shields.io/badge/Traefik-_?style=flat&logo=traefikproxy&logoColor=24A1C1&logoSize=auto&color=gray&labelColor=gray)](https://traefik.io/traefik)
[![Authelia](https://img.shields.io/badge/Authelia-_?style=flat&logo=authelia&logoColor=113155&logoSize=auto&color=gray&labelColor=gray)](https://www.authelia.com/)
[![Docker Socket Proxy](https://img.shields.io/badge/Docker_Socket_Proxy-_?style=flat&logo=docker&logoColor=2496ED&logoSize=auto&color=gray&labelColor=gray)](https://github.com/Tecnativa/docker-socket-proxy)

**Data Storage & Communication** \
[![Eclipse Mosquitto](https://img.shields.io/badge/Eclipse_Mosquitto-_?style=flat&logo=eclipsemosquitto&logoColor=3C5280&logoSize=auto&color=gray&labelColor=gray)](https://mosquitto.org/)
[![InfluxDB 3 Core](https://img.shields.io/badge/InfluxDB_3_Core-_?style=flat&logo=influxdb&logoColor=22ADF6&logoSize=auto&color=gray&labelColor=gray)](https://www.influxdata.com/products/influxdb/)
[![Media MTX](https://img.shields.io/badge/Media_MTX-_?style=flat&logo=&logoColor=1A65B7&logoSize=auto&color=gray&labelColor=gray)](https://mediamtx.org/)

**Monitoring & Metrics** \
[![Grafana OSS](https://img.shields.io/badge/Grafana_OSS-_?style=flat&logo=grafana&logoColor=F46800&logoSize=auto&color=gray&labelColor=gray)](https://grafana.com/oss/grafana/)
[![Telegraf](https://img.shields.io/badge/Telegraf-_?style=flat&logo=influxdb&logoColor=22ADF6&logoSize=auto&color=gray&labelColor=gray)](https://www.influxdata.com/time-series-platform/telegraf/)
[![MQTTX Web](https://img.shields.io/badge/MQTTX_Web-_?style=flat&logo=mqtt&logoColor=37DB86&logoSize=auto&color=gray&labelColor=gray)](https://mqttx.app/)

## Getting Started

### Requirements

 - Set up a Tailscale account (currently only tailscale.com is supported, support for custom control servers via headscale is planned)
   - Generate a one-time-use Auth Key for use as a secret later
 - Get a Porkbun domain (currently only Porkbun is supported as a PoC, domainless operation and other providers are planned).
   - Generate API credentials and store for use as secrets later
 - Clone the repository

### Configuration

The application is designed to be controlled exclusively with environment variables and secrets.

All secrets are expected to be files within a single folder. This folder can be set via environment variable (`SECRETS_DIR`) itself and defaults to `./.secrets` (git-ignored folder).

 - [List of environment variables](#env-vars)
 - [List of secrets](#secrets)

#### Shell Exports

The existing [.env](./.env) file contains sane defaults for most necessary environment variables and is designed to let you overwrite any of those environment variables via exports from your shell before running the application.

*Example:*
```sh
export APP_HOST="my-grow-box.example.com"
export APP_NAME_LABEL="MyGrowBox"
export TIMEZONE="Europe/Amsterdam"
export SECRETS_DIR="/run/secrets"
docker compose up
```

#### Repository ._env File

You can also create the file `._env` in the root directory of the cloned repository and instruct docker compose to use this file instead via the `--env-file` argument, i.e `docker compose up --env-file "./._env"` ([Compose documentation](https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/)).

> ℹ️ The file `._env` is included in [.gitignore](./.gitignore) and is guaranteed to not interfere with future updates via `git pull`.

> *⚠️
> If this method is used you need to define **all** necessary environment variables from the [.env](./.env) file, as docker compose will not use that file as a fallback, it is therefore recommended to copy the current `.env` file and replace all variable values.
> ⚠️*

*Example:* [See .env](./.env)

#### Local .env File

It is also possible to create a `.env` file in an unrelated directory ([Compose documentation](https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/#local-env-file-versus-project-directory-env-file)).

> ℹ️ In this case you need to set the additional variable `COMPOSE_FILE` to the path of the repository's compose file and all variables inside the [.env](./.env) file will be loaded as fallback, if your own `.env` file does not define them.

> ℹ️ You do not need to instruct docker compose to use this file as long as you run `docker compose up` from the directory containing your `.env` file.

*Example:*
```sh title="/path/to/your/.env"
# /path/to/your/.env
COMPOSE_FILE="/path/to/repository/compose.yml"
APP_HOST="my-grow-box.example.com"
APP_NAME_LABEL="MyGrowBox"
TIMEZONE="Europe/Amsterdam"
SECRETS_DIR="/run/secrets"
```

### Environment Variables {#env-vars}

At build-time Docker requires the following environment variables to be populated:

| Name | Description | Example | Default |
| :-- | :-- | :-- | :-- |
| `APP_HOST` | The main URL the device will be reachable at. | `my-grow-box.example.com` | *Empty* |
| `APP_NAME_HOST` | The prefix for all docker networks and containers, that this application will create. Also used as the internal hostname within all containers. | `my-grow-box` | `growzone` |
| `APP_NAME_LABEL` | The human readable name of the device. | `My GrowBox` | `Growzone` |
| `TIMEZONE` | Timezone identifier passed on to containers. | `Europe/Amsterdam` | `Europe/Berlin` |
| `VOLUME_DIR` | The directory in which [bind mounts](https://docs.docker.com/engine/storage/bind-mounts/) are placed *(Currently only named volumes are used)*. | `/path/to/my/volumes` | `./volumes` |
| `ENV_DIR` | The directory in which .env files for containers can be placed to override the default config. | `/path/to/my/env` | `./env.d` |
| `SECRETS_DIR` | The directory in which files containing secrets for containers are placed. | `/run/secret` | `./secrets` |

### Secrets {#secrets}

The following secrets must exist within the `SECRETS_DIR` directory at build-time, otherwise running the stack will fail.
They are expected to be files with the secret value being the content of the file.

| (File) Name | Description | Documentation / How to Obtain |
| :-- | :-- | :-- |
| `TS_AUTHKEY` | Authentication key to use to register the device in Tailscale when starting for the first time.[^1] | [Tailscale Docs](https://tailscale.com/docs/features/access-control/auth-keys) |
| `PORKBUN_API_KEY` | API key to prove domain ownership over `APP_HOST` via DNS challenge to Porkbun. | [Porkbun Docs](https://kb.porkbun.com/article/190-getting-started-with-the-porkbun-api) |
| `PORKBUN_API_SECRET_KEY` | API secret key to prove domain ownership over `APP_HOST` via DNS challenge to Porkbun. | [Porkbun Docs](https://kb.porkbun.com/article/190-getting-started-with-the-porkbun-api) |
| `AUTHELIA_OIDC_HMAC_SECRET` | Randomly generated HMAC key to secure OIDC. | [Authelia Docs: Generate Random Alphanumeric String](https://www.authelia.com/reference/guides/generating-secure-values/#generating-a-random-alphanumeric-string) |
| `AUTHELIA_OIDC_JWKS_KEY_PRIVATE` | Randomly generated private key to sign and verify OIDC tokens (multiline). | [Authelia Docs: Generate RSA Keypair](https://www.authelia.com/reference/guides/generating-secure-values/#generating-an-rsa-keypair) |
| `GRAFANA_OAUTH_CLIENT_ID` | Randomly generated OAuth client ID for Grafana. | [Authelia Docs: Generate Client ID](https://www.authelia.com/integration/openid-connect/frequently-asked-questions/#client-id--identifier) |
| `GRAFANA_OAUTH_CLIENT_SECRET` | Randomly generated OAuth client secret for Grafana. | [Authelia Docs: Generate Client Secret](https://www.authelia.com/integration/openid-connect/frequently-asked-questions/#client-secret) |
| `GRAFANA_OAUTH_CLIENT_SECRET_HASHED_PBKDF2` | PBKDF2 digest of `GRAFANA_OAUTH_CLIENT_SECRET`. | [Authelia Docs: Generate Client Secret](https://www.authelia.com/integration/openid-connect/frequently-asked-questions/#client-secret) |
| `LLDAP_JWT_SECRET` | Randomly generated string. | [LLDAP generate_secrets.sh](https://github.com/lldap/lldap/blob/main/generate_secrets.sh) |
| `LLDAP_KEY_SEED` | Randomly generated string. | [LLDAP generate_secrets.sh](https://github.com/lldap/lldap/blob/main/generate_secrets.sh) |
| `LLDAP_ADMIN_PASSWORD` | Password for the initial admin account. | Your preferred method. |
| `INFLUXDB_ADMIN_TOKEN_JSON` | The full admin token JSON for InfluxDB's first-time setup. | [InfluxDB Docs](https://docs.influxdata.com/influxdb3/enterprise/admin/tokens/admin/preconfigured/) |
| `INFLUXDB_ADMIN_TOKEN` | The token from the `token` field of the `INFLUXDB_ADMIN_TOKEN_JSON` secret. | [InfluxDB Docs](https://docs.influxdata.com/influxdb3/enterprise/admin/tokens/admin/preconfigured/) |

[^1]: It is advisable to use a one-time-use auth key and disable the key-expiry on the device once it has registered.

### Run the Application

 - Run `docker compose up` from the root directory of the repository or from the directory containing your `.env` file
 - Run `docker compose logs` and wait for the application to finish first-time setup and settle
 - Visit the domain set up via `APP_HOST` and login with username `admin` and the password set up via `LLDAP_ADMIN_PASSWORD`

## Acknowledgments and Licensing

This project is licensed under the [GNU Affero General Public License v3.0 (AGPL-3.0)](./LICENSE).

Copyright (c) 2026, GrowzoneTech and contributors. \
All rights reserved to the extent permitted by the AGPLv3.

For third-party license details and attribution, please see [Third-Party Licenses](./THIRD-PARTY-LICENSES.md).
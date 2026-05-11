[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue?style=flat)](./LICENSE)
![Development: Prototyping](https://img.shields.io/badge/Development-Prototyping-orange?style=flat)
![Version](https://img.shields.io/badge/dynamic/toml?label=Version&color=yellow&style=flat&url=https%3A%2F%2Fraw.githubusercontent.com%2Fgrowzone-tech%2Fgrowzone%2Frefs%2Fheads%2Fmain%2Fhardware-controller%2Fpkg%2Fpyproject.toml&query=%24.project.version)

# Growzone

> [!CAUTION]
> **🚧 This project is currently under heavy development, any information may be subject to change. 🚧**

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

## Getting Started

### Quick Start

 1. Configure the secrets needed for the modules
    - [Path](https://github.com/Tschebbischeff/habitat-path#secrets)
    - [Scent](https://github.com/Tschebbischeff/habitat-scent#secrets)
    - [Hoard](https://github.com/Tschebbischeff/habitat-hoard#secrets)
    - [Vigil](https://github.com/Tschebbischeff/habitat-vigil#secrets)
 2. Follow the [Habitat Quick Start Guide](https://github.com/Tschebbischeff/habitat#quick-start) and set the following environment variables in your `.env` file:
```sh
MODULE_LIST="path,scent,vista,chatter,hoard,vigil,sight,growzone-tech/growzone"
HABITAT_APP_NAME_HOST="growzone"
HABITAT_APP_NAME_LABEL="Growzone"
```

### Requirements

 - [![Habitat](https://img.shields.io/badge/Habitat--_?style=flat&color=gray&labelColor=gray)](https://github.com/Tschebbischeff/habitat)
 - [![Habitat-Module: Path](https://img.shields.io/badge/Habitat--Module-Path-_?style=flat&color=gray&labelColor=gray)](https://github.com/Tschebbischeff/habitat-path)
 - [![Habitat-Module: Scent](https://img.shields.io/badge/Habitat--Module-Scent-_?style=flat&color=gray&labelColor=gray)](https://github.com/Tschebbischeff/habitat-scent)
 - [![Habitat-Module: Vista](https://img.shields.io/badge/Habitat--Module-Vista-_?style=flat&color=gray&labelColor=gray)](https://github.com/Tschebbischeff/habitat-vista)
 - [![Habitat-Module: Chatter](https://img.shields.io/badge/Habitat--Module-Chatter-_?style=flat&color=gray&labelColor=gray)](https://github.com/Tschebbischeff/habitat-chatter)
 - [![Habitat-Module: Hoard](https://img.shields.io/badge/Habitat--Module-Hoard-_?style=flat&color=gray&labelColor=gray)](https://github.com/Tschebbischeff/habitat-hoard)
 - [![Habitat-Module: Vigil](https://img.shields.io/badge/Habitat--Module-Vigil-_?style=flat&color=gray&labelColor=gray)](https://github.com/Tschebbischeff/habitat-vigil)
 - [![Habitat-Module: Sight](https://img.shields.io/badge/Habitat--Module-Sight-_?style=flat&color=gray&labelColor=gray)](https://github.com/Tschebbischeff/habitat-sight)


### Configuration

> [!IMPORTANT]
> All habitat modules are designed to be controlled exclusively with environment variables and secrets. \
> Refer to the configuration section of each module for an overview of how to configure it. \
> **This section describes how to configure the module without the help of the [Habitat Deployment Service](https://github.com/Tschebbischeff/habitat). \
> It is highly recommended to use the deployment service for ease of use and skip to the lists of environment variables and secrets for this module.**

 - [List of environment variables](#environment-variables)
 - [List of secrets](#secrets)

#### Shell Exports

The existing [.env](./.env) file contains sane defaults for most necessary environment variables and is designed to let you overwrite any of those environment variables via exports from your shell before running the application.

*Example:*
```sh
export APP_HOST="my-grow-box.example.com"
export APP_MODULES="path,scent,vista,chatter,hoard,vigil,sight,growzone-tech/growzone"
export APP_SESSION_ID="$(cat /proc/sys/kernel/random/uuid)"
export APP_NAME_LABEL="MyGrowBox"
export TIMEZONE="Europe/Amsterdam"
export SECRETS_DIR="/run/secrets"
docker compose up
```

#### Repository _.env File

You can also create the file `_.env` in the root directory of the cloned repository and instruct docker compose to use this file instead via the `--env-file` argument, i.e `docker compose up --env-file "./_.env"` ([Compose documentation](https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/)).

> [!TIP]
> The file `_.env` is included in [.gitignore](./.gitignore) and is guaranteed to not interfere with future updates via `git pull`.

> [!IMPORTANT]
> *If this method is used you need to define **all** necessary environment variables from the [.env](./.env) file, as docker compose will not use that file as a fallback, it is therefore recommended to copy the current `.env` file and replace all variable values.*

*Example:* [See .env](./.env)

#### Local .env File

It is also possible to create a `.env` file in an unrelated directory ([Compose documentation](https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/#local-env-file-versus-project-directory-env-file)).

> [!NOTE]
> In this case you need to set the additional variable `COMPOSE_FILE` to the path of the repository's compose file and all variables inside the [.env](./.env) file will be loaded as fallback, if your own `.env` file does not define them.

> [!NOTE]
> You do not need to instruct docker compose to use this file as long as you run `docker compose up` from the directory containing your `.env` file.

*Example:*
```sh
# /path/to/your/.env
COMPOSE_FILE="/path/to/repository/compose.yml"
APP_HOST="my-grow-box.example.com"
APP_MODULES="path,scent,vista,chatter,hoard,vigil,sight,growzone-tech/growzone"
APP_SESSION_ID="$(cat /proc/sys/kernel/random/uuid)"
APP_NAME_LABEL="MyGrowBox"
TIMEZONE="Europe/Amsterdam"
SECRETS_DIR="/run/secrets"
```

### Environment Variables

At build-time Docker requires the following environment variables to be populated:

| Name | Description | Example | Default |
| :-- | :-- | :-- | :-- |
| `APP_HOST` | The main URL the device will be reachable at. | `my-grow-box.example.com` | *Empty* |
| `APP_MODULES` | A comma separated list of module names that are started in the same docker namespace (same project name) as this module. | `path,scent,vista,chatter,hoard,vigil,sight` | *Empty* |
| `APP_SESSION_ID` | A session ID used for synchronization of configuration between modules, should change every time all modules are restarted in unison and remain unchanged if a single module is restarted without being updated. | `$(cat /proc/sys/kernel/random/uuid)` | *Empty* |
| `APP_NETWORK_POOL` | The pool of IP addresses for the module containers, must match pool of all other modules in the same application. | `172.19.0.0/16` | `172.18.0.0/16` |
| `APP_NAME_HOST` | The prefix for all docker networks and containers, that this application will create. Also used as the internal hostname within all containers. | `my-grow-box` | `growzone` |
| `APP_NAME_LABEL` | The human readable name of the device. | `My GrowBox` | `Growzone` |
| `TIMEZONE` | Timezone identifier passed on to containers. | `Europe/Amsterdam` | `Europe/Berlin` |
| `VOLUME_DIR` | The directory in which [bind mounts](https://docs.docker.com/engine/storage/bind-mounts/) are placed *(Currently only named volumes are used)*. | `/path/to/my/volumes` | `./volumes` |
| `ENV_DIR` | The directory in which .env files for containers can be placed to override the default config. | `/path/to/my/env` | `./env.d` |
| `SECRETS_DIR` | The directory in which files containing secrets for containers are placed. | `/run/secret` | `./secrets` |

### Secrets

*This module does not require any secrets.*

<!--
> [!NOTE]
> All secrets are expected to be files within a single folder, each file containing the value of the secret. \
> This folder can be set via environment variable (`SECRETS_DIR`) itself and defaults to `./.secrets` (git-ignored folder). \
> All secrets must be present at run-time.

| (File) Name | Description | Documentation / How to Obtain |
| :-- | :-- | :-- |
|  | This module does not require any secrets |  |
-->

### Run the Application

 - Run `docker compose up` from the root directory of the repository or from the directory containing your `.env` file
 - Run `docker compose logs` and wait for the application to finish first-time setup and settle
 - Visit `${APP_HOST}` to see the main entry dashboard provided by the [Vista-Module](https://github.com/Tschebbischeff/habitat-vista)

## Supported Hardware

![TODO](https://img.shields.io/badge/TODO-Coming_Soon_(TM)-red?style=flat)

## Acknowledgments and Licensing

This project is licensed under the [GNU Affero General Public License v3.0 (AGPL-3.0)](./LICENSE).

Copyright (c) 2026, GrowzoneTech and contributors. \
All rights reserved to the extent permitted by the AGPLv3.

For third-party license details and attribution, please see [Third-Party Licenses](./THIRD-PARTY-LICENSES.md).

> [!WARNING]
> *Disclaimer:*
> This software controls hardware that may involve water and electricity. Use at your own risk. The developers and contributors are not responsible for any incurred damages or losses.
[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue?style=flat)](./LICENSE)
![Development: Prototyping](https://img.shields.io/badge/Development-Prototyping-orange?style=flat)
![Version](https://img.shields.io/badge/dynamic/toml?label=Version&color=yellow&style=flat&url=https%3A%2F%2Fraw.githubusercontent.com%2Fgrowzone-tech%2Fgrowzone%2Frefs%2Fheads%2Fmain%2Fhardware-controller%2Fpkg%2Fpyproject.toml&query=%24.project.version)

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
[![LLDAP](https://img.shields.io/badge/LLDAP-_?style=flat&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxODEuOSA3MCI+PGcgaWQ9InN2Z0dyb3VwIiBzdHJva2UtbGluZWNhcD0icm91bmQiIGZpbGwtcnVsZT0iZXZlbm9kZCIgZm9udC1zaXplPSI5cHQiIHN0cm9rZT0iIzIyMjIyMiIgc3Ryb2tlLXdpZHRoPSIwbW0iIGZpbGw9IiMyMjIyMjIiIHN0eWxlPSJzdHJva2U6IzIyMjIyMjtzdHJva2Utd2lkdGg6MG1tO2ZpbGw6IzIyMjIyMiI+PHBhdGggZD0iTSAwIDcwLjAwMSBMIDAgMC4wMDEgTCAxMSAwLjAwMSBMIDExIDYwLjAwMSBMIDI5LjEgNjAuMDAxIEwgMjkuMSA3MC4wMDEgTCAwIDcwLjAwMSBaIiBpZD0iMCIgdmVjdG9yLWVmZmVjdD0ibm9uLXNjYWxpbmctc3Ryb2tlIi8+PHBhdGggZD0iTSAzNC40IDcwLjAwMSBMIDM0LjQgMC4wMDEgTCA0NS40IDAuMDAxIEwgNDUuNCA2MC4wMDEgTCA2My41IDYwLjAwMSBMIDYzLjUgNzAuMDAxIEwgMzQuNCA3MC4wMDEgWiIgaWQ9IjEiIHZlY3Rvci1lZmZlY3Q9Im5vbi1zY2FsaW5nLXN0cm9rZSIvPjxwYXRoIGQ9Ik0gNjguOCA3MC4wMDEgTCA2OC44IDAuMDAxIEwgODUuNiAwLjAwMSBRIDkzLjggMC4wMDEgOTcuOSA0LjQwMSBRIDEwMiA4LjgwMSAxMDIgMTcuMzAxIEwgMTAyIDUyLjcwMSBRIDEwMiA2MS4yMDEgOTcuOSA2NS42MDEgUSA5My44IDcwLjAwMSA4NS42IDcwLjAwMSBMIDY4LjggNzAuMDAxIFogTSA3OS44IDYwLjAwMSBMIDg1LjQgNjAuMDAxIFEgODguMSA2MC4wMDEgODkuNTUgNTguNDAxIFEgOTEgNTYuODAxIDkxIDUzLjIwMSBMIDkxIDE2LjgwMSBRIDkxIDEzLjIwMSA4OS41NSAxMS42MDEgUSA4OC4xIDEwLjAwMSA4NS40IDEwLjAwMSBMIDc5LjggMTAuMDAxIEwgNzkuOCA2MC4wMDEgWiIgaWQ9IjIiIHZlY3Rvci1lZmZlY3Q9Im5vbi1zY2FsaW5nLXN0cm9rZSIvPjxwYXRoIGQ9Ik0gMTA2LjMgNzAuMDAxIEwgMTE3LjcgMC4wMDEgTCAxMzIuNiAwLjAwMSBMIDE0NCA3MC4wMDEgTCAxMzMgNzAuMDAxIEwgMTMxIDU2LjEwMSBMIDEzMSA1Ni4zMDEgTCAxMTguNSA1Ni4zMDEgTCAxMTYuNSA3MC4wMDEgTCAxMDYuMyA3MC4wMDEgWiBNIDExOS44IDQ2LjgwMSBMIDEyOS43IDQ2LjgwMSBMIDEyNC44IDEyLjIwMSBMIDEyNC42IDEyLjIwMSBMIDExOS44IDQ2LjgwMSBaIiBpZD0iMyIgdmVjdG9yLWVmZmVjdD0ibm9uLXNjYWxpbmctc3Ryb2tlIi8+PHBhdGggZD0iTSAxNDkuMyA3MC4wMDEgTCAxNDkuMyAwLjAwMSBMIDE2NS41IDAuMDAxIFEgMTczLjcgMC4wMDEgMTc3LjggNC40MDEgUSAxODEuOSA4LjgwMSAxODEuOSAxNy4zMDEgTCAxODEuOSAyNC4yMDEgUSAxODEuOSAzMi43MDEgMTc3LjggMzcuMTAxIFEgMTczLjcgNDEuNTAxIDE2NS41IDQxLjUwMSBMIDE2MC4zIDQxLjUwMSBMIDE2MC4zIDcwLjAwMSBMIDE0OS4zIDcwLjAwMSBaIE0gMTYwLjMgMzEuNTAxIEwgMTY1LjUgMzEuNTAxIFEgMTY4LjIgMzEuNTAxIDE2OS41NSAzMC4wMDEgUSAxNzAuOSAyOC41MDEgMTcwLjkgMjQuOTAxIEwgMTcwLjkgMTYuNjAxIFEgMTcwLjkgMTMuMDAxIDE2OS41NSAxMS41MDEgUSAxNjguMiAxMC4wMDEgMTY1LjUgMTAuMDAxIEwgMTYwLjMgMTAuMDAxIEwgMTYwLjMgMzEuNTAxIFoiIGlkPSI0IiB2ZWN0b3ItZWZmZWN0PSJub24tc2NhbGluZy1zdHJva2UiLz48L2c+PC9zdmc+&logoColor=EB5424&logoSize=auto&color=gray&labelColor=gray)](https://github.com/lldap/lldap)

**Networking & Security** \
[![Tailscale](https://img.shields.io/badge/Tailscale-_?style=flat&logo=tailscale&logoColor=242424&logoSize=auto&color=gray&labelColor=gray)](https://tailscale.com/)
[![Traefik](https://img.shields.io/badge/Traefik-_?style=flat&logo=traefikproxy&logoColor=24A1C1&logoSize=auto&color=gray&labelColor=gray)](https://traefik.io/traefik)
[![Authelia](https://img.shields.io/badge/Authelia-_?style=flat&logo=authelia&logoColor=113155&logoSize=auto&color=gray&labelColor=gray)](https://www.authelia.com/)
[![Docker Socket Proxy](https://img.shields.io/badge/Docker_Socket_Proxy-_?style=flat&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiMyNDk2RUQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBjbGFzcz0ibHVjaWRlIGx1Y2lkZS13YXlwb2ludHMtaWNvbiBsdWNpZGUtd2F5cG9pbnRzIj48cGF0aCBkPSJtMTAuNTg2IDUuNDE0LTUuMTcyIDUuMTcyIi8+PHBhdGggZD0ibTE4LjU4NiAxMy40MTQtNS4xNzIgNS4xNzIiLz48cGF0aCBkPSJNNiAxMmgxMiIvPjxjaXJjbGUgY3g9IjEyIiBjeT0iMjAiIHI9IjIiLz48Y2lyY2xlIGN4PSIxMiIgY3k9IjQiIHI9IjIiLz48Y2lyY2xlIGN4PSIyMCIgY3k9IjEyIiByPSIyIi8+PGNpcmNsZSBjeD0iNCIgY3k9IjEyIiByPSIyIi8+PC9zdmc+&logoColor=2496ED&logoSize=auto&color=gray&labelColor=gray)](https://github.com/Tecnativa/docker-socket-proxy)

**Data Storage & Communication** \
[![Eclipse Mosquitto](https://img.shields.io/badge/Eclipse_Mosquitto-_?style=flat&logo=eclipsemosquitto&logoColor=3C5280&logoSize=auto&color=gray&labelColor=gray)](https://mosquitto.org/)
[![InfluxDB 3 Core](https://img.shields.io/badge/InfluxDB_3_Core-_?style=flat&logo=influxdb&logoColor=22ADF6&logoSize=auto&color=gray&labelColor=gray)](https://www.influxdata.com/products/influxdb/)
[![Media MTX](https://img.shields.io/badge/Media_MTX-_?style=flat&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiMxQTY1QjciIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBjbGFzcz0ibHVjaWRlIGx1Y2lkZS1jYW1lcmEtaWNvbiBsdWNpZGUtY2FtZXJhIj48cGF0aCBkPSJNMTMuOTk3IDRhMiAyIDAgMCAxIDEuNzYgMS4wNWwuNDg2LjlBMiAyIDAgMCAwIDE4LjAwMyA3SDIwYTIgMiAwIDAgMSAyIDJ2OWEyIDIgMCAwIDEtMiAySDRhMiAyIDAgMCAxLTItMlY5YTIgMiAwIDAgMSAyLTJoMS45OTdhMiAyIDAgMCAwIDEuNzU5LTEuMDQ4bC40ODktLjkwNEEyIDIgMCAwIDEgMTAuMDA0IDR6Ii8+PGNpcmNsZSBjeD0iMTIiIGN5PSIxMyIgcj0iMyIvPjwvc3ZnPg==&logoColor=1A65B7&logoSize=auto&color=gray&labelColor=gray)](https://mediamtx.org/)

**Monitoring & Metrics** \
[![Grafana OSS](https://img.shields.io/badge/Grafana_OSS-_?style=flat&logo=grafana&logoColor=F46800&logoSize=auto&color=gray&labelColor=gray)](https://grafana.com/oss/grafana/)
[![Telegraf](https://img.shields.io/badge/Telegraf-_?style=flat&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdCb3g9IjEwIDEwIDc1IDc2Ij48cGF0aCBmaWxsPSIjMDIwQTQ3IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Im02Ni4wMDcgNjEuOTQyIDE3LjQwMi0zLjk4MWMuMjU1LS4wODUuNTEtLjE3Ljc2Ni0uMjk3YTEuOCAxLjggMCAwIDAgLjU1My0uNTkyYy4xMjgtLjI1NS4yNTUtLjUwOS4yNTUtLjc2My4wNDMtLjI1NCAwLS41NS0uMDg1LS44MDRsLTcuNDAzLTMxLjkzYy0uMTI4LS41NTEtLjQ2OC0uOTc1LS45MzYtMS4yNzEtLjQ2OC0uMjU0LTEuMDIyLS4zODEtMS41NzUtLjI1NGwtMTcuNDAyIDMuOThhMi4xNiAyLjE2IDAgMCAwLTEuMjc3LjkzMmMtLjI1NS40NjYtLjM4MyAxLjAxNy0uMjU1IDEuNTY3bDcuMzYxIDMxLjkzYy4xMjguNTUxLjQ2OC45NzQuOTM2IDEuMjcuNTk2LjI1NSAxLjE0OS4zNCAxLjY2LjIxM20tNS45NTYgMjAuNTc1IDIxLjQ3LTIwLjQ0Yy43OC0uODQ2LjYwNy0xLjMzNi0uNTItLjkzNWwtMTQuNzkgMy40NzNhMy41NCAzLjU0IDAgMCAwLTEuNjQ5Ljg5MSA0LjMgNC4zIDAgMCAwLS45OTcgMS42MDNsLTQuNDY4IDE0LjgzYy0uMzA0IDEuMTEzLjEzIDEuNDI0Ljk1NC41NzhNMjAuNDg2IDc2LjE0bDMyLjM1OSA5LjgyOGMuNTY3LjA4NiAxLjEzNCAwIDEuNjE0LS4yNTguNDgtLjI1Ny44NzItLjczIDEuMDQ2LTEuMjQ0bDUuNDA4LTE3LjA4Yy4wODctLjI1Ny4wODctLjU1Ny4wODctLjgxNS0uMDQ0LS4yNTctLjA4Ny0uNTU4LS4yNjItLjc3Mi0uMTMtLjI1OC0uMzA1LS40My0uNTIzLS42MDEtLjIxOC0uMTcyLS40OC0uMy0uNzQxLS4zODZMMjcuMTE1IDU1LjA3Yy0uNTY3LS4xMjgtMS4xMzQtLjA4Ni0xLjY1Ny4xNzItLjQ4LjI1Ny0uODcyLjczLTEuMDAzIDEuMjg3TDE5LjA5IDczLjUyM2EyIDIgMCAwIDAgLjE3NCAxLjU4OGMuMjYyLjUxNS42OTguOTAxIDEuMjIxIDEuMDNNMTAuMDg3IDQwLjk3M2w2LjQyOSAyOC4xOTNjLjIxMyAxLjExMi43MjMgMS4xMTIuOTc5IDBMMjEuODggNTQuOTJjLjEyOC0uNi4xNy0xLjI0LjA0My0xLjg0LS4xMjgtLjU5OS0uNDI2LTEuMTU1LS44MS0xLjYyNUwxMS4wMjQgNDAuNDZjLS43MjQtLjc3LTEuMjM1LS41NTYtLjkzNy41MTNNMzUuMTg2IDEwLjUzIDEwLjY1MyAzMy43ODVhMi4zNiAyLjM2IDAgMCAwLS42NDggMS40NTYgMS45MiAxLjkyIDAgMCAwIC41NjIgMS41bDEyLjMxIDEzLjU5MmMuMzg4LjQ0LjkwNy42MTcgMS40NjguNjYxLjU2Mi4wNDUgMS4wOC0uMTc2IDEuNDY5LS41NzNsMjQuNTMzLTIzLjI1NWEyLjM2IDIuMzYgMCAwIDAgLjY0OC0xLjQ1NyAxLjkyIDEuOTIgMCAwIDAtLjU2Mi0xLjVMMzguMTY3IDEwLjY2MmMtLjE3My0uMjItLjQzMi0uMzUzLS42NDgtLjQ4Ni0uMjYtLjA4OC0uNTE5LS4xNzYtLjc3OC0uMTc2cy0uNTYxLjA0NC0uNzc3LjEzMmExLjIyIDEuMjIgMCAwIDAtLjc3OC4zOThtMjQuMjIxIDUxLjM5NGMxLjEzLjI5OSAxLjgyNi0uMyAxLjUyMS0xLjQ1M0w1My44IDMwLjA2Yy0uMzA0LTEuMTExLTEuMjE3LTEuNDEtMi4wNDMtLjU5OGwtMjMuMjU1IDIxLjI3Yy0uODI2Ljc3LS42MDkgMS43MDkuNDc4IDEuOTY1ek03MS4xODUgMTkuMjFsLTI4LjItOS4xMDNjLTEuMTMtLjMyLTEuMzA0LjA5MS0uNDM1IDEuMDUybDEwLjI5OCAxMS43MWMuNDM1LjQ1NyAxIC43NzcgMS42NTEuOTYuNjA5LjE4MyAxLjI2LjIyOCAxLjg2OS4wOTFsMTQuODE3LTMuNTIyYzEuMDg3LS4zMiAxLjA4Ny0uODY5IDAtMS4xODkiIGNsaXAtcnVsZT0iZXZlbm9kZCIvPjwvc3ZnPg==&logoColor=22ADF6&logoSize=auto&color=gray&labelColor=gray)](https://www.influxdata.com/time-series-platform/telegraf/)
[![MQTTX Web](https://img.shields.io/badge/MQTTX_Web-_?style=flat&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjQwIDIyIDI0MCAyNzciPjxnIGZpbGw9IiMwMEIxNzMiIGZpbGwtcnVsZT0iZXZlbm9kZCI+PHBhdGggZD0iTTIxNC44IDEwNy4wODdIMTEyLjQ5NnYuMDIxYy0uMTQyLS4wMDYtLjI4Mi0uMDIxLS40MjUtLjAyMS01LjMxMSAwLTkuNjE2IDQuMjkzLTkuNjE2IDkuNTg5IDAgNS4yOTUgNC4zMDUgOS41ODggOS42MTYgOS41ODguMTQzIDAgLjI4My0uMDE1LjQyNS0uMDIydi4wMjJIMjE0LjhjNS4zMSAwIDkuNjE1LTQuMjkzIDkuNjE1LTkuNTg4IDAtNS4yOTYtNC4zMDUtOS41OS05LjYxNS05LjU5bTAgOTEuMzQxSDExMi40OTZ2LjAyYy0uMTQyLS4wMDUtLjI4Mi0uMDItLjQyNS0uMDItNS4zMTEgMC05LjYxNiA0LjI5My05LjYxNiA5LjU4OHM0LjMwNSA5LjU4OCA5LjYxNiA5LjU4OGMuMTQzIDAgLjI4My0uMDE1LjQyNS0uMDJ2LjAySDIxNC44YzUuMzEgMCA5LjYxNS00LjI5MyA5LjYxNS05LjU4OHMtNC4zMDUtOS41ODgtOS42MTUtOS41ODhtLTI2Ljg3Ni0zNi4wODJjMC01LTMuODQtOS4xMDEtOC43MzktOS41NDV2LS4wNDRoLTg3Ljcydi4wMjJjLS4xNDItLjAwNi0uMjgxLS4wMjItLjQyNS0uMDIyLTUuMzEgMC05LjYxNSA0LjI5My05LjYxNSA5LjU5IDAgNS4yOTUgNC4zMDUgOS41ODggOS42MTUgOS41ODguMTQ0IDAgLjI4My0uMDE2LjQyNi0uMDIydi4wMjJoODcuNzE5di0uMDQ1YzQuODk5LS40NDIgOC43MzktNC41NDQgOC43MzktOS41NDQiLz48cGF0aCBmaWxsLXJ1bGU9Im5vbnplcm8iIGQ9Ik0yODAgOTEuMjUgMTYwIDIyIDQwIDkxLjI1djEzOC41TDE2MCAyOTlsMTIwLTY5LjI1ek0xNjAgNDIuNzEybDEwMi4wNDkgNTguODk0VjIxOS4zOEwxNjAgMjc4LjI3NiA1Ny45MzkgMjE5LjM4VjEwMS42MDZ6Ii8+PC9nPjwvc3ZnPg==&logoColor=37DB86&logoSize=auto&color=gray&labelColor=gray)](https://mqttx.app/)

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

 - [List of environment variables](#environment-variables)
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
```sh
# /path/to/your/.env
COMPOSE_FILE="/path/to/repository/compose.yml"
APP_HOST="my-grow-box.example.com"
APP_NAME_LABEL="MyGrowBox"
TIMEZONE="Europe/Amsterdam"
SECRETS_DIR="/run/secrets"
```

### Environment Variables

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

### Secrets

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

## Supported Hardware

![TODO](https://img.shields.io/badge/TODO-Coming_Soon_(TM)-red?style=flat)

## Acknowledgments and Licensing

This project is licensed under the [GNU Affero General Public License v3.0 (AGPL-3.0)](./LICENSE).

Copyright (c) 2026, GrowzoneTech and contributors. \
All rights reserved to the extent permitted by the AGPLv3.

For third-party license details and attribution, please see [Third-Party Licenses](./THIRD-PARTY-LICENSES.md).

With Icons from:
[![SimpleIcons](https://img.shields.io/badge/SimpleIcons-_?style=flat&logo=simpleicons&logoColor=111111&logoSize=auto&color=gray&labelColor=gray)](https://simpleicons.org/)
[![DashboardIcons](https://img.shields.io/badge/DashboardIcons-_?style=flat&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Qm94PSIwIDAgMjMyIDIzMiIgcm9sZT0iaW1nIiBhcmlhLWxhYmVsPSJkYXNoYm9hcmQtaWNvbnMgbG9nbyI+DQogIDxyZWN0IHg9IjQiIHk9IjQiIHdpZHRoPSIyMjQiIGhlaWdodD0iMjI0IiByeD0iMzIiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzAwMCIgc3Ryb2tlLXdpZHRoPSI4IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiLz4NCiAgPGcgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjY2NjIiBzdHJva2Utd2lkdGg9IjQiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+DQogICAgPHJlY3QgeD0iMjQiIHk9IjI0IiB3aWR0aD0iNDgiIGhlaWdodD0iNDgiIHJ4PSI4IiBzdHJva2U9IiNGQjcxODUiLz4NCiAgICA8cmVjdCB4PSI5MiIgeT0iMjQiIHdpZHRoPSI0OCIgaGVpZ2h0PSI0OCIgcng9IjgiIGZpbGw9IiNGREJBNzQiLz4NCiAgICA8cmVjdCB4PSI5MiIgeT0iOTIiIHdpZHRoPSI0OCIgaGVpZ2h0PSI0OCIgcng9IjgiIHN0cm9rZT0iI0M0QjVGRCIvPg0KICAgIDxyZWN0IHg9IjE2MCIgeT0iOTIiIHdpZHRoPSI0OCIgaGVpZ2h0PSI0OCIgcng9IjgiLz4NCiAgICA8cmVjdCB4PSI5MiIgeT0iMTYwIiB3aWR0aD0iNDgiIGhlaWdodD0iNDgiIHJ4PSI4Ii8+DQogICAgPHJlY3QgeD0iMTYwIiB5PSIxNjAiIHdpZHRoPSI0OCIgaGVpZ2h0PSI0OCIgcng9IjgiIGZpbGw9IiM5M0M1RkQiLz4NCiAgPC9nPg0KICA8Y2lyY2xlIGN4PSIxODQiIGN5PSI0OCIgcj0iMjYiIGZpbGw9IiM4NkVGQUMiLz4NCiAgPGNpcmNsZSBjeD0iNDgiIGN5PSIxMTYiIHI9IjI2IiBmaWxsPSIjOTNDNUZEIi8+DQogIDxyZWN0IHg9IjI0IiB5PSIxNjAiIHdpZHRoPSI0OCIgaGVpZ2h0PSI0OCIgcng9IjgiIGZpbGw9IiNGREU2OEEiLz4NCjwvc3ZnPg==&logoColor=F56565&logoSize=auto&color=gray&labelColor=gray)](https://dashboardicons.com/)
[![Lucide](https://img.shields.io/badge/Lucide-_?style=flat&logo=lucide&logoColor=F56565&logoSize=auto&color=gray&labelColor=gray)](https://lucide.dev/)
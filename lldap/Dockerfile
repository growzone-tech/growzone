FROM lldap/lldap:stable

RUN apk add envsubst

COPY ./entrypoint-hook.sh /entrypoint-hook.sh
RUN chmod +x /entrypoint-hook.sh

ENTRYPOINT ["/entrypoint-hook.sh"]
CMD ["/docker-entrypoint.sh", "run", "--config-file", "/data/lldap_config.toml"]
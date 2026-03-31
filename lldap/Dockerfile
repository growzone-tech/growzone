FROM lldap/lldap:stable

COPY ./entrypoint-hook.sh /entrypoint-hook.sh
RUN chmod +x /entrypoint-hook.sh

ENTRYPOINT ["/entrypoint-hook.sh"]
CMD ["/app/docker-entrypoint.sh", "run", "--config-file", "/data/lldap_config.toml"]
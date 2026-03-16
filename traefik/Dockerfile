FROM traefik:latest

COPY ./entrypoint-hook.sh /entrypoint-hook.sh
RUN chmod +x /entrypoint-hook.sh

CMD ["sh", "-c", "/entrypoint-hook.sh"]
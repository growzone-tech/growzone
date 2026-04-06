FROM bluenviron/mediamtx:latest AS mediamtx
FROM alpine:latest

COPY --from=mediamtx /mediamtx /
COPY --from=mediamtx /mediamtx.yml /

RUN apk add wget

ENTRYPOINT [ "/mediamtx" ]
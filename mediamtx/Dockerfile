FROM bluenviron/mediamtx:latest AS mediamtx
FROM alpine:latest

COPY --from=mediamtx /mediamtx /
COPY --from=mediamtx /mediamtx.yml /

RUN apk add wget
RUN apk add v4l-utils

ENTRYPOINT [ "/mediamtx" ]
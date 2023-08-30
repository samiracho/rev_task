#python:3.10-alpine3.18
FROM python@sha256:159a916f08f6895ddb572a47ec36278eb19123c87774cc6807c7f702cb3080a7
WORKDIR /app
ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0 --workers=1"
ADD requirements.txt .

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

ADD src/. .

CMD ["gunicorn", "app:app"]
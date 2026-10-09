FROM python:3.12-slim

WORKDIR /app

COPY app.py .

RUN mkdir -p /data

VOLUME ["/data"]

ENTRYPOINT ["python", "app.py"]

CMD ["list"]
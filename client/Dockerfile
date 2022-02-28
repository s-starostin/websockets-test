FROM python:3.10-alpine
WORKDIR /app
COPY ./ /app
RUN pip install asyncio websockets
CMD ["python", "websocket-client.py"]

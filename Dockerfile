# FROM alpine:latest
# RUN apk add --no-cache python3-dev \
#     && pip3 install --upgrade pip
# FROM python:3
# COPY requirement.txt ./

# RUN pip install --no-cache-dir -r requirement.txt
# COPY . .
# ENTRYPOINT [ "python" ]
# CMD [ "server.py" ]

FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirement.txt
ENTRYPOINT ["python"]
CMD ["server.py"]

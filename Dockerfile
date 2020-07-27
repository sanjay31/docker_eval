FROM python:3

WORKDIR /usr/src/app

COPY mac_addr_lookup.py .

ENTRYPOINT ["python", "./mac_addr_lookup.py"]

CMD ["--ApiKey XXXXXXXXXXXXXXXXXXX --MacAddress XXXXXXXXXXXXXX"]

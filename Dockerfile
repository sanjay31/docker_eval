FROM python:3

WORKDIR /usr/src/app

COPY mac_addr_lookup.py .

ENTRYPOINT ["python", "./mac_addr_lookup.py"]

CMD ["--ApiKey at_l14boXSI4bfjG54kLmtdOsIAVXqC1 --MacAddress 58-91-CF-24-A0-9F"]

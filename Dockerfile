FROM python:alpine3.16 as compile-image
RUN apk add --no-cache gcc linux-headers libc-dev musl-dev python3-dev openldap-dev openssl-dev xmlsec expat libffi-dev cargo && apk upgrade --no-cache
# Build venv
RUN python -m venv /opt/venv
# Make sure we use the venv:
ENV PATH="/opt/venv/bin:$PATH"
# install requirements in venv
COPY requirements.txt .
RUN pip3 install --no-cache-dir -U pip && pip3 install --no-cache-dir -r requirements.txt


FROM python:alpine3.16
# retrieve previously built venv
COPY --from=compile-image /opt/venv /opt/venv
# Make sure we use the venv:
ENV PATH="/opt/venv/bin:$PATH"
COPY . /app
WORKDIR /app
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
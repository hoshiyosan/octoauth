FROM python:3.8-alpine

WORKDIR /octoauth

# Copy production requirements
COPY requirements/production /tmp/requirements

# Install packages required to build dependencies, then remove it
RUN apk add --no-cache g++ gcc musl-dev                     \
    && pip install --no-cache-dir -r /tmp/requirements      \
    && apk del g++ gcc musl-dev

COPY octoauth/ /octoauth/octoauth

ENV OCTOAUTH_ENV=production

CMD [ "uvicorn", "octoauth.application:api", "--port", "80"]

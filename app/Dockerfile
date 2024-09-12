FROM python:3.12.5-slim

ARG USERNAME=te_backend
ARG USER_UID=1000
ARG USER_GID=${USER_UID}

RUN apt-get update && \
    apt-get install -y libpq-dev gcc

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

USER ${USERNAME}

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
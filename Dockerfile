FROM python:3.8.0a3-alpine

# Install LibreOffice
RUN apk add --no-cache libreoffice libreoffice-common

# Install fontconfig to manage fonts
RUN apk add --no-cache fontconfig

# Copy the fonts to container
COPY ./fonts /usr/share/fonts

# Refresh the font cache
RUN fc-cache -f -v

# Install any other dependencies
RUN apk add --no-cache py3-pip && pip install --no-cache-dir glob2

COPY ./src /usr/src/app

WORKDIR /usr/src/app

RUN chmod +x main.py

ENTRYPOINT ["python", "main.py"]

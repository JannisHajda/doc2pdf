FROM python:3.12.6-alpine

# Install LibreOffice and fontconfig 
RUN apk add --no-cache \
    libreoffice \
    libreoffice-common \
    fontconfig \
    && rm -rf /var/cache/apk/*

# Install gcc, musl-dev, and other dependencies needed for pip packages
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev

# Upgrade pip and install tqdm
RUN pip install --upgrade pip && pip install tqdm

# Copy the fonts to the container
COPY ./fonts /usr/share/fonts

# Refresh the font cache
RUN fc-cache -f -v

# Copy application data and change the working directory
COPY ./src /usr/src/app
WORKDIR /usr/src/app

# Set the entrypoint to run the Python script
ENTRYPOINT ["python", "main.py"]

FROM python:3.11-slim

WORKDIR /app

RUN apt-get update -yq \
    && apt-get install -y \
    curl \
    unzip \
    libglib2.0-0 \
    libnss3 \
    libxcb1 \
    libdbus-1-3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libxkbcommon0 \
    libpango1.0-0 \
    libasound2 \
    && rm -rf /var/lib/apt/lists/*

# ENV CHROME_URL=https://storage.googleapis.com/chrome-for-testing-public
# ENV CHROME_VER=123.0.6312.105
# RUN curl -sSLO ${CHROME_URL}/${CHROME_VER}/linux64/chrome-linux64.zip \
#     && unzip ./chrome-linux64.zip -d chrome \
#     && curl -sSLO ${CHROME_URL}/${CHROME_VER}/linux64/chromedriver-linux64.zip \
#     && unzip ./chromedriver-linux64.zip -d chrome \
#     && rm -f ./chrome-linux64.zip ./chromedriver-linux64.zip

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

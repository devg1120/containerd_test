FROM python:3


WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt install -y tzdata && apt-get clean && rm -rf /var/lib/apt/lists/* 
ENV TZ Asia/Tokyo

COPY . .



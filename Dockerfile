FROM python:3.7

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY ../../../Desktop /usr/src/app/
RUN apt update
EXPOSE 8888
RUN apt-get install -y sendfile ffmpeg libavcodec-extra sox
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "start.py"]
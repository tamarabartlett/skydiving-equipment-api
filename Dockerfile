FROM alpine
MAINTAINER tamjbart@gmail.com
FROM python:3.7

WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
ENV FLASK_APP api.py

CMD ["flask", "run", "--host", "0.0.0.0"]

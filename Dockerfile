FROM python:3.7
MAINTAINER Marco Marinho
ADD . /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY entrypoint.sh /entrypoint.sh
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
RUN chmod 755 /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
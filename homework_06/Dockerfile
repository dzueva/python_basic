FROM tiangolo/uwsgi-nginx-flask:python3.11

RUN pip3 install --upgrade pip
COPY /requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

COPY ./app/ ./
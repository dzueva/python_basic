FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /var/app

RUN pip3 install --upgrade pip
COPY /requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

COPY main.py .

CMD uvicorn main:app --host=0.0.0.0 --port 8000
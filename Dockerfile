FROM python:3.9

WORKDIR /application

COPY ./requirements.txt /application

RUN pip install -r ./requirements.txt

COPY . /application

EXPOSE 8000

CMD ["python", "./app/backend/paymentapp_server.py"]


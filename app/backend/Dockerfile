FROM python:3.9

WORKDIR /paymentapp/app

COPY ./requirements.txt /paymentapp/app

RUN pip install -r ./requirements.txt

COPY . /paymentapp/app

CMD ["python", "./main.py"]
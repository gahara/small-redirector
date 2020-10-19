FROM python:3.8.5

RUN mkdir /code

COPY requirements.txt /code

RUN pip install -r /code/requirements.txt

COPY . /code

WORKDIR /code

CMD flask run --host 0.0.0.0
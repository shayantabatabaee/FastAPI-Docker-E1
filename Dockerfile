FROM python:3.7-slim

RUN mkdir /code
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/

ENV FAST_API_ENV=production

CMD ["python", "asgi.py"]


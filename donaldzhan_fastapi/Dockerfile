FROM python:3.9.13-alpine3.15
LABEL Author Donald Zhan<donald.zhan1984@gmail.com>
LABEL Maintainer Donald Zhan<donald.zhan1984@gmail.com>

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host","0.0.0.0", "--port", "80"]
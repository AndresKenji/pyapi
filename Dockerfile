FROM python:3.12.4-alpine

RUN apk update \ apk upgrade
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN rm requirements.txt

COPY /app /app
WORKDIR /app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
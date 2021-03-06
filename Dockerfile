FROM python:3.10

 WORKDIR /app

COPY ./requirements.txt /app

RUN pip install -r ./requirements.txt

COPY ./src /app/src

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host=0.0.0.0", "--reload"]
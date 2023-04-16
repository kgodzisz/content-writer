FROM python:3.9-slim-buster

WORKDIR /app

COPY cw.py .

RUN pip install docx2txt

ENTRYPOINT ["python", "cw.py"]

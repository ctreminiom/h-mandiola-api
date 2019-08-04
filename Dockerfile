FROM python:3.6-alpine

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN mkdir assets/

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "index"]
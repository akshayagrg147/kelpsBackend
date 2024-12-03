FROM python:3.11

ENV PYTHONUNBUFFERED 1

RUN echo "Building the Docker image for my application..."

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8010

CMD ["python", "manage.py", "runserver", "0.0.0.0:8010"]

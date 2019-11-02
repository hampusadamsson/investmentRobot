FROM python:3.7-alpine

RUN apk add g++ 
RUN pip install numpy

WORKDIR /app


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "/app/src/Simulation.py"]

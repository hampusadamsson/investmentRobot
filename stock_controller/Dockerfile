FROM python:3.7-alpine

RUN apk add g++
RUN pip install numpy

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

WORKDIR /src/controller/

ENTRYPOINT ["python3"]
CMD ["app.py"]
# CMD ["top"]

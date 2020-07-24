FROM python:3.8

COPY . /breastcancerapp

WORKDIR /breastcancerapp

RUN apt-get update -y && apt-get install python3-pip idle3 -y && pip3 install --no-cache-dir --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 5000

CMD python app.py
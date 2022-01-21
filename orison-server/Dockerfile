FROM python:3.9.4

WORKDIR /orison-server

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP=flaskr
ENV FLASK_ENV=development

RUN [ "python3", "-m" , "flask", "init-db"]

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
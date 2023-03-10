FROM python:3.8-slim-buster

WORKDIR /python-docker

RUN pip install flask
RUN pip install bs4
RUN pip install requests

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
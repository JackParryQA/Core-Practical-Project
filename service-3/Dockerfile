FROM python

RUN apt-get update
RUN apt install python-pip -y

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5002

ENTRYPOINT ["python3","app.py"]

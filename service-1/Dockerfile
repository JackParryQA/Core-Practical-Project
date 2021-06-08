FROM python

RUN apt-get update
RUN apt install python-pip -y

ENV DATABASE_URI = 'mysql+pymysql://root:root@35.204.240.245:MLBDraft'

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3","app.py"]

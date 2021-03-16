# first stage
FROM python:3.8

#COPY requirements.txt .

ADD main.py .

# install dependencies to the local user directory (eg. /root/.local)
RUN pip install regex pandas 

CMD [ "python", "./main.py" ]
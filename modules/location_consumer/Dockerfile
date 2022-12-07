FROM python:3.7-alpine

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5005

COPY . .
CMD ["python", "receiver.py"]
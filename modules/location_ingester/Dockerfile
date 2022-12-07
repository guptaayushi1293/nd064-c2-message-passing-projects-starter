FROM python:3.7-alpine

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN apk add --no-cache gcc python3-dev
RUN apk add build-base linux-headers
RUN pip install -r requirements.txt

EXPOSE 5005

COPY . .
CMD ["python", "main.py"]
#Base Image
FROM python:3.11-slim

#set working directory
WORKDIR /app

#Copy Files in container
COPY . /app

#Install dependencies
RUN pip install -r requirements.txt

#cmd to run your APP
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
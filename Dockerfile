#Base Image
FROM python=3.11-slim

#set working directory
WORKDIR /app

#Copy Files in container
COPY . /app

#Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#cms to run your APP
CMD ["python","run.py"]
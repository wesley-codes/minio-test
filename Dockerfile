FROM python:3.10-slim 
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY file_uploader.py .
RUN echo 'Hello MinIO from Kubernetes' > /tmp/test.txt
CMD [ "python", "file_uploader.py" ]

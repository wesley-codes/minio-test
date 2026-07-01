import os
from dotenv import load_dotenv
from minio import Minio

load_dotenv()
client = Minio(
    os.getenv("MINIO_ENDPOINT"),
    access_key = os.getenv("MINIO_ACCESS_KEY"),
    secret_key = os.getenv("MINIO_SECRET_KEY"),
    secure = False      
)

buckets = client.list_buckets()
print("Connected. Buckets:", [bucket.name for bucket in buckets])
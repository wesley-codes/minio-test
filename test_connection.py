import os
from dotenv import load_dotenv
from minio import Minio

load_dotenv()

def main():
    client = Minio(
    os.getenv("MINIO_ENDPOINT"),
    access_key = os.getenv("MINIO_ACCESS_KEY"),
    secret_key = os.getenv("MINIO_SECRET_KEY"),
    secure = False      
)
    source_file = "/tmp/test.txt"
    bucket_name = "test-bucket"
    destination_file = "test.txt"
    
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)
        print(f"{bucket_name} created")
    else:
        print(f"{bucket_name} already exists")
    # buckets = client.list_buckets()

if __name__ == "__main__":
    try:
        main()
    except S3Error as e:
        print("Error:", "An Error Occured")
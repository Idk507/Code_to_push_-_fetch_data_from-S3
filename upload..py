
def upload_to_s3(local_file, bucket, s3_file):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_KEY,
        aws_secret_access_key=AWS_SECRET
    )
    try:
        s3_client.upload_file(local_file, bucket, s3_file)
        print(f"Upload Successful: {s3_file}")
        return True
    except FileNotFoundError:
        print(f"The file {local_file} was not found")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


bucket_name = ""
upload_to_s3("1_document.pdf", bucket_name, "1_document")
upload_to_s3("2_document.pdf", bucket_name, "2_document")

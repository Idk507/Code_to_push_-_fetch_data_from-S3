import boto3
from botocore.exceptions import NoCredentialsError
from datetime import datetime, timedelta




def get_s3_document_info(bucket_name, file_key):
    try:
        
        s3_client = boto3.client(
            's3',
            aws_access_key_id=AWS_KEY,
            aws_secret_access_key=AWS_SECRET
        )

        response = s3_client.head_object(Bucket=bucket_name, Key=file_key)
        

        presigned_url = s3_client.generate_presigned_url('get_object',
                                                        Params={'Bucket': bucket_name,
                                                               'Key': file_key},
                                                        ExpiresIn=3600)
        

        doc_info = {
            'file_name': file_key,
            'bucket': bucket_name,
            's3_uri': f's3://{bucket_name}/{file_key}',
            'presigned_url': presigned_url,
            'size_bytes': response['ContentLength'],
            'last_modified': response['LastModified'],
            'etag': response['ETag'].strip('"')
        }
        
        return doc_info
    
    except Exception as e:
        print(f"Error getting document info: {str(e)}")
        return None



documents = ["1_document", "2_document"]
for doc in documents:
    print(f"\nGetting info for {doc}:")
    doc_info = get_s3_document_info(bucket_name, doc)
    if doc_info:b  
        print("Document Details:")
        print(f"S3 URI: {doc_info['s3_uri']}")
        print(f"Presigned URL (expires in 1 hour): {doc_info['presigned_url']}")
        print(f"Size: {doc_info['size_bytes']} bytes")
        print(f"Last Modified: {doc_info['last_modified']}")
        print(f"ETag: {doc_info['etag']}")

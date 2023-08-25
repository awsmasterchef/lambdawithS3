import boto3

def lambda_handler(event, context):
    # Replace 'your-bucket-name' and 'your-file-key' with actual values
    bucket_name = 'your-bucket-name'
    file_key = 'your-file-key'
        
    byte_range = f'bytes=12-100'
    
    # Create an S3 client
    s3_client = boto3.client('s3')
    
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=file_key, Range=byte_range)
        byte_range_content = response['Body'].read().decode('utf-8')
        print(byte_range_content)
        
        return {
            'statusCode': 200,
            'body': 'Byte range retrieved successfully'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }

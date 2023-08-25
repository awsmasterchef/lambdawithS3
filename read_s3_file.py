import boto3

def lambda_handler(event, context):
    # Replace 'your-bucket-name' and 'your-file-key' with actual values
    bucket_name = 'your-bucket-name'
    file_key = 'your-file-key'
    
    # Create an S3 client
    s3_client = boto3.client('s3')
    
    try:
        # Retrieve the file from S3
        response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        
        # Read the content of the file
        file_content = response['Body'].read().decode('utf-8')
        
        # Do something with the file content
        # For example, print the content
        print(file_content)
        
        return {
            'statusCode': 200,
            'body': 'File content retrieved successfully'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }

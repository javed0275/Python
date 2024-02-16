
import boto3
import os
def upload_to_dynamodb(table_name,s3_bucket,s3_key):
    #set up AWS credentials & Dynamodb client
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(table_name)
    
    #Download the file from S3 to a temporary  location on disk
    tmp_file= '/temp/temp-file.txt'  # use a temporary file to store the s3 file 
    s3 = boto3.client('s3')
    s3.download_file(s3_bucket,s3_key,tmp_file)
    
    
    #Read data from the temporary file 
    
    with  open (tmp_file,'r') as file:
          data = file .read()
          
          
    # update DynamoDB table.
    
    response = table.put_item(Item={"key":"value", #replace with your actual attribute and values.
                                    "Another key":"Another Value"})  
    
    # Print the response from Dynamodb
    
    print("Dynamodb update response:", response)
    #clean up the temporary file
    os.remove (tmp_file)
    
    if __name__ == "__main__":
        
    #replace with your DynamoDB table name,s3 bucket ,and s3 key 
    
    table_name = "your Dynamo DB table Name"
    s3_bucket = "Your S3 bucket name"
    s3_key = "YourS3Objectkey"
    
    try:
        #call the function to update Dynamodb
        upload_to_dynamodb(table_name,s3_bucket,s3_key)
        print("update successful")
        
    except NoCredentials Error:
        print("credentials not available.Make sure your AWS credentials are properly configured")
    except Exception as e:
        print(f"An error occurred :{e}")
        
        
        
                                    
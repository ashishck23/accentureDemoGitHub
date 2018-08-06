import boto3
s3=boto3.resource('s3')
#bucket=s3.Bucket('com.accenture.ashish.bucket.test1')


#Create an S3 Client
#s3=boto3.client('s3')
#se=boto3.resource('s3')

filename='myfile.txt'
bucket_name='com.accenture.ashish.bucket.test1'

#upload
try: 
 #response=s3.upload_file(filename,bucket_name,'myfile_uploaded.txt')
 response=s3.Bucket('com.accenture.ashish.bucket.test1').download_file('age.py','myfile_downloaded.txt')
 print(response)
except Exception as error:
 print(error)

 
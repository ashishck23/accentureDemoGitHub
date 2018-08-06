import boto3

ec2=boto3.resource('ec2')
instance=ec2.Instance('i-0b48a9f0e7ef67e3a')

#instance.start()
response=instance.report_status(

Status='ok'|'impaired'
)

print(response)
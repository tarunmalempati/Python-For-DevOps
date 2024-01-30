import boto3

ec2 = boto3.resource('ec2')
ids = ['string'] #insert instance ids separated by commas

response = ec2.instances.filter(InstanceIds = ids).terminate()
print(response)

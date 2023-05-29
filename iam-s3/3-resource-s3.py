import boto3
s3 = boto3.client('s3')
bucket_name = 'codealongbucketjigsaw'

response = s3.get_bucket_acl(Bucket=bucket_name)
bucket_acl = response['Grants']

s3.put_object(Body='Text Contents', Bucket=bucket_name, Key='example.txt')

# Retrieve the bucket policy
bucket_policy = s3.get_bucket_policy(Bucket=bucket_name)
view_policy = bucket_policy['Policy']



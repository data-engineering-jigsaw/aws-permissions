import boto3
import os

# Create an IAM client
iam_client = boto3.client('iam')

# Get the current user
response = iam_client.get_user()

# # Access the user details
username = response['User']['UserName']
print("User Name:", username)

response = iam_client.list_attached_user_policies(UserName=username)
attached_policies = response['AttachedPolicies']
print('attached_policies', attached_policies)

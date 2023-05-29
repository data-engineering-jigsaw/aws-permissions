# Print the bucket policy and ACL
print("Bucket Policy:")
print(bucket_policy)

print("\nBucket ACL:")
for grant in bucket_acl:
    print(grant)


# IAM policies define what a principal can do in your AWS environment

# s3 policies
    #  Next we need to see the iam access list
    # This seems to have some good information on access control lists
    # https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingObjects.html#access-control


# s3.list_objects_v2(Bucket = 'data-eng-careers')
    # Note that we can list ojects from a bucket from the same account

    

# s3.put_object(Body='Text Contents', Bucket='data-eng-careers', Key='example.txt')
    # And apparently we can also put information to that bucket (for a publicly available bucket)
    # but is allowed to add information to a publicly available bucket


# s3.list_objects_v2(Bucket = 'data-eng-careers')
    # Note that we can list ojects from a bucket we created



# Now what if we specify a policy on the bucket
# Sample User policy

# {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Effect": "Allow",
#             "Principal": {
#                 "AWS": "arn:aws:iam::086729879076:user/sample-user"
#             },
#             "Action": [
#                 "s3:GetObject",
#                 "s3:ListBucket"
#             ],
#             "Resource": [
#                 "arn:aws:s3:::jigsaw-initial-bucket",
#                 "arn:aws:s3:::jigsaw-initial-bucket/*"
#             ]
#         }
#     ]
# }

# s3.list_objects_v2(Bucket = 'jigsaw-initial-bucket')

# s3.put_object(Body='Text Contents', Bucket='jigsaw-initial-bucket', Key='ok.txt')

# so for the sample-user
    # put object access was denied, once we removed it from the bucket policy.  And then allowed for that user.
    # 


# But if we explicitly deny access, then we will see it's denied, even if we give s3 access.
# {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Effect": "Deny",
#             "NotPrincipal": {
#                 "AWS": "arn:aws:iam::086729879076:user/aws-access"
#             },
#             "Action": "s3:*",
#             "Resource": [
#                 "arn:aws:s3:::jigsaw-initial-bucket",
#                 "arn:aws:s3:::jigsaw-initial-bucket/*"
#             ]
#         }
#     ]
# }

# So in summary with the permission slip, and bouncer idea
    # If the bouncer has a deny, then it will deny (even if there's a permission slip)
    # If the bouncer has an allow, then it will allow, even if there is no permission slip
    # If the bouncer does not have an allow, but there is a permission slip, then ok.

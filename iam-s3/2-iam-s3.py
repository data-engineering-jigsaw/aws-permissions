# s3 = boto3.client('s3')

# s3.create_bucket(Bucket = 'jigsawspecialsample') Access denied

# s3.list_objects_v2(Bucket = 'jigsawtxdrinks')
    # # Note that we can list ojects from a bucket from the same account

# s3.put_object(Body='Text Contents', Bucket='jigsawtxdrinks', Key='example.txt')
    # For an bucket that is not publicly accessible, we cannot add a new object

    # For that we would need to use an iam policy that has put access permissions
    # This time when we switched back to admin access, we were able to add a new object


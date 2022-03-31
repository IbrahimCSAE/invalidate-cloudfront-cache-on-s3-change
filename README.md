# invalidate-cloudfront-cache-on-s3-change


• Python Lambda function to invalidate CloudFront cache whenever the S3 bucket gets updated manually or via code pipeline.

# Steps


• set S3 objectcreated events as a trigger to the Lambda function
• edit the IAM role for the lambda function to allow it to interact with CloudFront




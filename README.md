# Invalidate CloudFront cache whenever S3 bucket gets updated


• Python Lambda function to invalidate CloudFront cache whenever the S3 bucket gets updated manually or via code pipeline.

# Steps


• set S3 objectcreated events as a trigger to the Lambda function </br>
• edit the IAM role for the lambda function to allow it to interact with CloudFront </br>




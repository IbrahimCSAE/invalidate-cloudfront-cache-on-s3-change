# Invalidate CloudFront cache whenever S3 bucket gets updated


• Python Lambda function to invalidate CloudFront cache whenever you update your S3 bucket via code pipeline. </br>

# Steps


• Go to Code Pipeline, add stage, add action, select action provider as invoke AWS Lambda, select the lambda function. </br>
• Edit the IAM role for the lambda function to allow it to interact with CloudFront and Code Pipeline </br>
• All done! </br>




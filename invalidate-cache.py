from __future__ import print_function

import boto3
import time

def lambda_handler(event, context):
    path = ["/"]
    client = boto3.client('cloudfront')
    invalidation = client.create_invalidation(DistributionId='E33J1W1JUL5EDB',
        InvalidationBatch={
            'Paths': {
                'Quantity': 1,
                'Items': path
        },
        'CallerReference': str(time.time())
    })

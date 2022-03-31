
from __future__ import print_function

import boto3
import time
import json
import logging

def lambda_handler(event, context):
    path = ["/*"]
    client = boto3.client('cloudfront')
    invalidation = client.create_invalidation(DistributionId='E33J1W1JUL5EDB',
        InvalidationBatch={
            'Paths': {
                'Quantity': 1,
                'Items': path
        },
        'CallerReference': str(time.time())
    })
    invalidation_id = invalidation['Invalidation']['Id']
    
    print("Invalidation created successfully with Id: " + invalidation_id)
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.debug(json.dumps(event))
 
    codepipeline = boto3.client('codepipeline')
    job_id = event['CodePipeline.job']['id']
 
    try:
        logger.info('Success!')
        response = codepipeline.put_job_success_result(jobId=job_id)
        logger.debug(response)
    except Exception as error:
        logger.exception(error)
        response = codepipeline.put_job_failure_result(
            jobId=job_id,
            failureDetails={
              'type': 'JobFailed',
              'message': f'{error.__class__.__name__}: {str(error)}'
            }
        )
        logger.debug(response)

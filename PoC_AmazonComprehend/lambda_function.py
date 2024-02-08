import json
import boto3
import pandas as pd
import io
import datetime as dt

from comprehend_sentiment_analysis import sentiment_analysis

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    comprehend = boto3.client('comprehend')
    bucket_name='poc-comprehend-sentiment-analysis'

    response = s3.get_object(Bucket=bucket_name, Key='input/data.csv')
    d0 = pd.read_csv(io.BytesIO(response['Body'].read()))
    d0['Comment'] = d0['Comment'].str.replace('\n', '')
    d0['Comment'] = d0['Comment'].str.replace('\u3000', '')
    print('read data completed')

    # 1) remove empty records, 2) implement sentiment analysis, 3) merge data, and 4) save it as csv file
    data_to_analysis = d0.dropna(subset=['Comment']).reset_index(drop=True)
    d1=sentiment_analysis(data_to_analysis)
    df_return = pd.merge(d0,d1,on='ID',how='left')
    df_return.to_csv('/tmp/df_return.csv', index=False)

    # upload s3
    current_time = dt.datetime.now(dt.timezone(dt.timedelta(hours=9))).strftime('%Y%m%d%H%M') # Japanese time
    file_key = 'output/' + current_time + '_sentiment_analysis.csv'
    s3.upload_file('/tmp/df_return.csv', bucket_name, file_key)
    print('s3 upload completed')

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Amazon Comprehend Sentiment Analysis Completed')
    }

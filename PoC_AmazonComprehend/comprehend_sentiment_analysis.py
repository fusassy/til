import boto3
import pandas as pd
import numpy as np

def sentiment_analysis(data):
    '''
    Input: コメントが入った行のみのデータフレーム (回答なしのデータを除外済み)
    Output: 各コメントのSentimentとそのScoreの列が追加されたデータフレーム
    '''
    comprehend = boto3.client('comprehend')

    sentiment_list = []

    for comment in data['Comment']:
        # identify dominant language
        language = comprehend.detect_dominant_language(Text=comment)

        # detect sentiment
        comment_sentiment = comprehend.detect_sentiment(Text=comment, LanguageCode=language['Languages'][0]['LanguageCode'])
        sentiment_list.append(comment_sentiment)

    print('comprehend job completed')

    df_sentiment = pd.json_normalize(sentiment_list)
    df_sentiment = df_sentiment.iloc[:, 0:4] # select main sentiment and each score (positive/negative/mixed/neutral)
    df_sentiment['Score'] = df_sentiment.max(axis='columns')
    df_sentiment = df_sentiment[['Sentiment', 'Score']]

    data = pd.concat([data, df_sentiment], axis=1)
    df_return = data[['ID', 'Sentiment', 'Score']]

    return df_return

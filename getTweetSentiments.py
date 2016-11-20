import tweepy
import json
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    password="3ey2hUOvMXYz",
    username="159be137-d864-46d9-8c2a-7583979d6f58",
    version="2016-11-17")

consumer_key = "1GxDEzabtR40NQ5cZyBlmE4PI"
consumer_secret = "zVDh15NKvTS1rBBKgLy56bMSi1ajPxJM5LhxiU7ABZ0zkMvjJR"
access_token = "1319670133-ZLbk21ReodUzeVDY5bzNezei6FuAsB9Gy4SxEAk"
access_token_secret = "qPUUH7wPIuWtGkgspjfaJzorqBlrrH3kRxEZpMMkLD8wF"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

results = api.search(q="snow",geocode="40,-83,30mi", count=10)

for a in results:
    parsed_string = json.dumps(a._json)
    parsed = json.loads(parsed_string)
    if str(parsed['coordinates']) != "None" or str(parsed['place']) != "None":
        tweet_text = parsed['text']
        print(tweet_text)
        watson_response = json.dumps(tone_analyzer.tone(text=str(parsed['text'])))
        watson_parsed = json.loads(watson_response)
        print(watson_parsed['document_tone']['tone_categories'][0]['tones'][0])
        print(watson_parsed['document_tone']['tone_categories'][0]['tones'][1])
        print(watson_parsed['document_tone']['tone_categories'][0]['tones'][2])
        print(watson_parsed['document_tone']['tone_categories'][0]['tones'][3])
        print()

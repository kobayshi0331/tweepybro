import tweepy
import time

CK = 'LMeBLV7gTEzB6wCJK9ZVU0LZo'
CS = 'ytnFUZQHu1hg58xRWg2RuZwgHvycML1OZt5UFPN0fmJXhplxeI'
AT = '1500314688231391235-lXk8jqd1947MGmaF4jhQeBThga1tuo'
AS = '1OoGXFelTIslouOrVSE2H50yd5rdn7dB1ULVTEZQUKNoE'

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

q= 'リツイート min_retweets:500 -filter:follows'
results=api.search_tweets(q=q, count=15,result_type='recent')

for result in results:
    screen_name = result.user.screen_name
    id  = result.id
    print('@' + screen_name + 'をフォロー処理中...')
    for i in range(3): #RateLimitにかかったら3回までリトライ
        try:
            if result.lang == 'ja':
                api.create_favorite(id)
                api.create_friendship(screen_name=screen_name)
                api.retweet(id)
                print('@' + screen_name + 'さんのフォロー、リツイート、いいねに成功しました。')
            else:
                print('@' + screen_name + 'さんは日本語アカウントではありません。')
        except tweepy.TweepError as e:
            if e.reason == "[{'message': 'Rate limit exceeded', 'code': 88}]":
               print(e)
               time.sleep(15 * 60) #15分待機
            else:
               break
        else:
            time.sleep(5)
            break
        

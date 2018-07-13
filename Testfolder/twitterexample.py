import json

f = open("twitterdata.json", "r")
tweetData = json.load(f)
f.close()

for tweet in tweetData:
    print("Tweet text:" + tweet["text"])

for id in range(len(tweetdata)):
    print(tweetData[id]["id"])

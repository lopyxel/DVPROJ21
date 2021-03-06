from flask import Flask, render_template, request
import csv
import pandas as pd
import VDRSM as vs;
import tweepy
import Graphic as graphDraw


API_KEY = "oicq8ITFxrufAMoBHJ8hyvlLl"
API_SECRET = "Ko7yh0Dh7rvu1FJ0VjYonc7eJooOlstW9w97t5sBv94YAklNSV"
AccessToken = "1440589328913031178-Mn1bNDjrsfKj2E7tUo3iHrZb3VA3Eg"
accessTokenSecret = "5qOvJu2UnDwOZoq3K5jUBjV0W0Lo1BfaoegkvSSvsdNfl"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(AccessToken, accessTokenSecret)

api = tweepy.API(auth)

app = Flask(__name__)

#cursor = tweepy.Cursor(api.user_timeline, id='elonmusk', tweet_mode="extended").items(1)

numTweets = 40
tweets = []
likes = []
time = []
location = []
tweetNum = []

for i in tweepy.Cursor(api.user_timeline, id='elonmusk', tweet_mode="extended").items(numTweets):
    tweets.append(i.full_text + " *_*")
    likes.append(i.favorite_count)
    time.append(i.created_at)
    location.append(i.geo)

df = pd.DataFrame({'tweets':tweets, 'likes':likes, 'time':time, 'location':location})
df = df[~df.tweets.str.contains("RT")] #filtering out retweets
df = df.reset_index(drop = True)

for i in range(len(tweets)):
    #print(i, " " , tweets[i])
    tweetNum.append(i)

with open('static/CSV/variables.csv', 'w', encoding="utf-8", newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(tweets)
    sentdata = vs.sentimentRating(tweets)
    csvwriter.writerow(sentdata)


ratings = sentdata[0]
#print(len(ratings), " " , len(tweetNum))
graphDraw.drawBasicGraph(tweetNum, ratings, "Tweets","Positivity Level","Tweet Ratings")
mostLikedTweets = df.loc[df.likes.nlargest(5).index]
#print(mostLikedTweets)

#read into vdr sentiment
#write sentiment data out to csv file
#use csv data to output to graphs on a website.


@app.route('/', methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        print(request.form["inputId"])
    return render_template('index.html')

@app.route('/about', methods=["GET"])
def aboutpage():
    return render_template("about.html")

@app.route('/charts', methods=["GET"])
def chartspage():
    return render_template("charts.html")

@app.route('/charts', methods=["POST"])
def tweetspage():  # put application's code here
    if request.method == 'POST':
        query = request.form["query"]
        graphDraw.setInputLable(str(query))
        tweets0 = []
        likes0 = []
        time0 = []
        location0 = []
        tweetIndices = []
        TI = 0;
        for i in tweepy.Cursor(api.search_tweets, q=query, tweet_mode="extended").items(numTweets):
            TI = TI + 1
            tweets0.append(i.full_text + " *_*")
            likes0.append(i.favorite_count)
            time0.append(i.created_at)
            location0.append(i.geo)
            tweetIndices.append(TI)
        df2 = pd.DataFrame({'tweet': tweets0, 'likes': likes0, 'time': time0, 'location': location0})
        df2 = df2[~df2.tweet.str.contains("RT")]  # filtering out retweets
        df2 = df2.reset_index(drop=True)
        with open('static/CSV/tweet.csv', 'w', encoding="utf-8", newline='') as f:
            thewriter = csv.writer(f)
            thewriter.writerow(tweets0)
            ratedData = vs.sentimentRating(tweets0)
            thewriter.writerow(ratedData)
        graphDraw.compareBasicGraphs(tweetNum, ratings, "Tweets","Positivity Level","tweet ratings", tweetIndices, ratedData[0])
        return render_template('charts.html', query = tweets)
    return render_template('404.html')

if __name__ == '__main__':
    app.run()




from vader_sentiment.vader_sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob


text = "I LOVE EXISTANCE!"
analyser = SentimentIntensityAnalyzer()
blob = TextBlob(text)
levels = []
scores = []

print("Textblob output: ", blob.sentiment.polarity)  # much less accurate


def sentiment_analyser_score(data):
    score = analyser.polarity_scores(data)
    # print("{:-<40} {}".format(data,str(score)))
    print(score)



def sentimentRating(data):#requires a list of texts, even of len 1
    for i in data:
        print(i," of" ,len(data))
        score = analyser.polarity_scores(i).get('compound')
        level = ""
        if score < -0.7:
            level = "Super Negative"
        if -0.3 > score > -0.7:
            level = "Negative"
        if 0.3 > score > -0.3:
            level = "Neutral"
        if 0.7 > score > 0.3:
            level = "Positive"
        if 0.7 < score:
            level = "Super Positive"
        scores.append(score)
        levels.append(level)
    dataSend = [scores, levels]
    print(dataSend)
    return dataSend


# sentiment_analyser_score(text)
data = ["whats up my guy", "fuck you richard(MEME)", "I love existence "]
sentimentRating(data)


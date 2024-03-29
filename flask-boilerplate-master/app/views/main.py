from flask import render_template, jsonify
from app import app
import random
import tweepy
import TextBlob

#login twitter - auth code

consumer_key = ''
consumer_secret = ''

access_token = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/search',methods=['POST'])
def search():
	search_tweet = request.form.get('search_query')
	alltweets = []
	tweets = api.search(search_tweet)
	for tweet in tweets:
		polarity = TextBlob(tweet.full_text).sentiment.polarity
		subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
		alltweets.append([tweet.full_text, polarity, subjectivity])

	return jsonify({'Success':True, 'Tweets':alltweets})

@app.route('/map')
def map():
    return render_template('map.html', title='Map')


@app.route('/map/refresh', methods=['POST'])
def map_refresh():
    points = [(random.uniform(48.8434100, 48.8634100),
               random.uniform(2.3388000, 2.3588000))
              for _ in range(random.randint(2, 9))]
    return jsonify({'points': points})


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

import tweepy
import statistics
from textblob import TextBlob

class SentimentResult:
	POSITIVE = "Positive"
	NEUTRAL = "Neutral"
	NEGATIVE = "Negative"

	def __init__(self, pos, neg, neu, mean, variance):
		self.singleTweetSentiment = dict()
		self.singleTweetSentiment[SentimentResult.POSITIVE] = pos
		self.singleTweetSentiment[SentimentResult.NEGATIVE] = neg
		self.singleTweetSentiment[SentimentResult.NEUTRAL] = neu
		self.mean = mean
		self.variance = variance


class SentimentAnalysis:
	
	def __init__(self):
		# Twitter keys and tokens
		self.consumer_key = 	'N53GGMD69iViFNjirSqX6RBl1'
		self.consumer_secret = 'VoioAOXhOL28ejd6x0yPq5clIHppKZk4QyGOMKbOxJ7mQ88cnr'
		self.access_token = '935065354438660097-YDjz3m9YwbkZYgMtxQAm3RATMzewGja'
		self.access_token_secret = 'biVPOWWVVFVu7BG2T6CXBK2ibPgTMyFjskMNNuZJtOVH2'

		#times a call to the API is made
		self.times = 3          

		#Authentication for api
		self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		self.auth.set_access_token(self.access_token, self.access_token_secret)

		#call to web service
		self.api = tweepy.API(self.auth)


	def getSentimentValues(self, keyWord):
		#results
		public_tweets = self.api.search(keyWord)
		
		sentimentValues = []

		#calculate sentiment
		for tweet in public_tweets:
			if tweet.lang == "en":
				analysis = TextBlob(tweet.text)
				sentimentValues.append(analysis.sentiment.polarity)

		return sentimentValues


	def classify(self, sentiment):
		if sentiment < -0.1:
			return SentimentResult.NEGATIVE
		elif sentiment > 0.1:
			return SentimentResult.POSITIVE
		else:
			return SentimentResult.NEUTRAL


	def classifySingleTweetSentiments(self, sentimentValues):
		pos = neg = neu = 0

		for sentiment in sentimentValues:
			result = self.classify(sentiment)

			if result == SentimentResult.POSITIVE:
				pos += 1

			elif result == SentimentResult.NEGATIVE:
				neg += 1

			else:
				neu += 1

		return (pos, neg, neu)


	def calculateStatistics(self, sentimentValues):
		mean = statistics.mean(sentimentValues)
		variance = statistics.variance(sentimentValues)
		return (mean, variance)


	def getSentiment(self, keyWord):
		sentiments = []

		for i in range(0, self.times):
			(sentimentValues) = self.getSentimentValues(keyWord)
			sentiments.extend(sentimentValues)

		(mean, variance) = self.calculateStatistics(sentimentValues)
		(pos, neg, neu) = self.classifySingleTweetSentiments(sentimentValues)

		return SentimentResult(pos, neg, neu, mean, variance)


if __name__ == '__main__':
    analysis = SentimentAnalysis()
    result = analysis.getSentiment('sad')
    print(result.singleTweetSentiment)
    print(result.mean)
    print(result.variance)
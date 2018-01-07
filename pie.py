import matplotlib.pyplot as plt
import sentiment_analysis

class Graph:
	def __init__(self):
		self.labels = ('Positive', 'Negative', 'Neutral')
		self.colors = ['green', 'red', 'yellow']
		self.sizes = []

	def setData(self, data):
		self.sizes = data

	def plotData(self, title, positives, negatives, neutrals, mean, variance):
		plt.pie(self.sizes, labels=self.labels, colors=self.colors,
		        autopct='%1.1f%%', shadow=True, startangle=140)
		plt.title("Phrase: " + title + "\n" + 
			"#pos: " + str(positives) + 
			"    #neg: " + str(negatives) + 
			"    #neu: " + str(neutrals) + 
			"    Mean: " + str(round(mean, 2)) + 
			"    Variance: " + str(round(variance, 2)))
		plt.axis('equal')
		plt.show()
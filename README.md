TWITTER SENTIMENT ANALYSIS
===

STEP 1: What is sentiment analysis, and why should you care about it? 😄 😐 😭
---	
  Sentiment analysis is the process of determining the emotional tone behind a series of words, used to gain an understanding of the the attitudes, opinions and emotions expressed within an online mention.
	Sentiment analysis is extremely useful in social media monitoring as it allows us to gain an overview of the wider public opinion behind certain topics. The applications are broad and powerful. The ability to extract insights from social data is a practice that is being widely adopted by organisations across the world.  
Fun fact: 
The Obama administration used sentiment analysis to gauge public opinion to policy announcements and campaign messages ahead of 2012 presidential election.😎

STEP 2: Wiring up! 🔌
---
For this project you will need:
* Raspberry Pi (in our case: Raspberry Pi 3 Model B)
* 3 LED diodes (green, yellow and red) for representing the mood, calculated from the sentiment analysis
* 3 resistors (in our case 330 Ohm) to protect your GPIO pins
* jump wires

Now, you have to connect the led diodes on the specific GPIO pins on the Raspberry Pi (you can choose other pins, but you will have to refactor the code afterwards).

Make sure you Raspberry Pi is turned off. Then, connect the resistors on the anodes of the LED diodes. After that, you should connect your green diode on the pin 21, yellow on the pin 24 and the red on the pin 15. All of the cathodes should be connected to the Ground pins. Now you are all set to jump on the next step!

STEP 3: Import the packages 🚚
---
You'll need a couple of packages in order for the code to work.
* Tweepy: python library for the official Twitter API.
	pip3 install tweepy
* TextBlob: python library for processing textual data.
	pip3 install textblob
* Pillow: python library for the user interface.
	pip3 install pillow

The following packages usually come bundled with python3, but in case you get compilation error, simply install them using the pip3 command:
* Statistics: python library for statistics.
* Matplotlib: python library for graphics representation of data.
* Tkinter: python library for the user interface.
* RPi.GPIO: python library that's available only on a RaspberryPi (but hey, we're doing this for a RasberryPi exclusively), that manages the GPIO pins.

*NOTE*: In order to test this on desktop: simply comment out 'import led_manager.py' in the main.py script.

STEP 4: Implementation 🛠
---
Place the following scripts together in a directory on the RaspberryPi:

* main.py - The entry point for the app. (run this script in the console).
* sentiment_analysis.py - Script that connects to the Twitter API, processes the data and generates results.
* pie.py - Script that generates a graphic representation of the results.
* led_manager.py - Script that handles the diodes on the RaspberryPi.

*Contributors*: **Zafir Stojanovski (151015) & Filip Spasovski (151049)**

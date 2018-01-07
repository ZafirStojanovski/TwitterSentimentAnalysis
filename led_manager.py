import RPi.GPIO as GPIO

class LEDManager:

	def __init__(self):
		#set mode
		GPIO.setmode(GPIO.BCM)

		#colors
		self.red = 15
		self.yellow = 24
		self.green = 21

		#set I/O of pins
		GPIO.setup(red, GPIO.OUT)
		GPIO.setup(yellow, GPIO.OUT)
		GPIO.setup(green, GPIO.OUT)

	def turnOffAll(self):
		GPIO.output(red, False)
		GPIO.output(yellow, False)
		GPIO.output(green, False)

	def turnOnRed(self):
		self.turnOffAll()
		GPIO.output(red, True)

	def turnOnYellow(self):
		self.turnOffAll()
		GPIO.output(yellow, True)

	def turnOnGreen(self):
		self.turnOffAll()
		GPIO.output(green, True)
class Day:
	def __init__(self, inHour, outHour):
		self._inHour = inHour
		self._outHour = outHour

	# getter method
	def get_inHour(self):
		return self._inHour

	def get_outHour(self):
		return self._outHour
		
	# setter method
	def set_inHour(self, x):
		self._inHour = x

	def set_outHour(self, x):
		self._outHour = x
from obj.Day import Day

class Person:
	def __init__(self, name):
		self._name = name
		self._days = [Day(-1,-1),Day(-1,-1),Day(-1,-1),Day(-1,-1),Day(-1,-1),Day(-1,-1),Day(-1,-1),]
		
	# getter method
	def get_name(self):
		return self._name

	def get_day(self, id):
		return self._days[id].get_inHour(), self._days[id].get_outHour()
		
	# setter method
	def set_name(self, x):
		self._name = x

	def set_day(self, id, inHour, outHour):
		self._days[id].set_inHour(inHour)
		self._days[id].set_outHour(outHour)
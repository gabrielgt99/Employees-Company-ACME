from obj.Person import Person

def readData(name_file):
	# Read files
	file = open('/home/runner/Employees-Company-ACME/data/{}.txt'.format(name_file),'r')
	case = file.read()
	file.close()
	return case

def dataCleaning(case, persons):
	# Split persons
	case = case.split('\n')
	
	# Loop for person
	for i in range(len(case)):
		# Find the name and days position
		limit = (case[i].find('='))
		name = case[i][:limit]
		days = case[i][limit+1:]

		# Split days
		days = days.split(',')

		# appending instances to list 
		persons.append( Person(name) )

		days_id = {
			"MO": 0,
			"TU": 1,
			"WE": 2,
			"TH": 3,
			"FR": 4,
			"SA": 5,
			"SU": 6,
		}

		for j in range(len(days)):
			# convert to minutes
			# totalMinutes = (h*60+m)
			# ex. 10:30, 10*60+30
			inHour = int(days[j][2:].split('-')[0].split(':')[0]) * 60 + int(days[j][2:].split('-')[0].split(':')[1])
			outHour = int(days[j][2:].split('-')[1].split(':')[0]) * 60 + int(days[j][2:].split('-')[1].split(':')[1])
			
			persons[i].set_day(days_id[days[j][:2]], inHour, outHour)

def checkSchedule(persons, id1, id2):
	coincidences = 0

	# 7 days a week loop for each employee
	for i in range(7):
		personA = persons[id1].get_day(i)
		personB = persons[id2].get_day(i)
	
		# Determine if the employee is working that day
		# Identify which of the two employees started first
		# Subtraction, to determine if the two employees can meet
		if(personA[0] != -1 and personA[1] != -1 and personB[0] != -1 and personB[1] != -1):
			if(personA[0] < personB[0]):
				if(personA[1] - personB[0] > 0):
					coincidences += 1
			else:
				if(personB[1] - personA[0] > 0):
					coincidences += 1
	return persons[id1].get_name(), persons[id2].get_name(),coincidences

def main():

	# Read text file, find the number of employees
	case1 = readData('case1')
	cases1_len = len(case1.split('\n'))
	
	# case2 = readData('case2')
	# cases2_len = len(case2.split('\n'))

	persons = []

	case1 = dataCleaning(case1, persons)

	for i in range(0, cases1_len-1):
		for j in range(1, cases1_len):
			if (i != j):
				ans = checkSchedule(persons, i, j)
				print("{}-{}: {}".format(ans[0], ans[1], ans[2]))	

if __name__ == "__main__":
    main()
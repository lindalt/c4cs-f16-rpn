#!/usr/bin/env python

def print_welcome():
	print("Welcome to the simple test program")

def compute_time(current_month):
	# Winter months means no work can happen
	WINTER = (0, 1, 2, 10, 11) # Jan, Feb, Mar, .., Nov, Dec

	# List of (todo, months)
	TODO = (
			('Finish Molds',  3),
			('New Topsoil',   2),
			('New Sidewalks', 2),
			('Install WiFi',  1),
			('Plant Trees',   2),
			)
	months = 0
	for todo in TODO:
		while (current_month % 12) in WINTER:
			months += 1
			current_month += 1
		months += todo[1]
		current_month += todo[1]
	return months

def pretty_print(current_month, current_year, months_to_go):
	def month_to_season(month):
		if month in (11,0,1):
			return 'Winter'
		if month in (2,3,4):
			return 'Spring'
		if month in (5,6,7):
			return 'Summer'
		if month in (8,9,10):
			return 'Fall'
		raise NotImplementedError("Illegal month")

	year = current_year + int(months_to_go / 12)
	month = current_month + months_to_go % 12

	return month_to_season(month) + ' ' + str(year) + '.'

if __name__ == '__main__':
	print_welcome()
<<<<<<< HEAD
	print('')
	print('According to current estimates, the diag construction will be done:')
	print('Never.')

=======
	time = compute_time(2) # 2 is March
	print(pretty_print(2, 2016, time))
>>>>>>> remotes/origin/merge_me

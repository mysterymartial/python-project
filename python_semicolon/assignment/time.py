def seconds_since_midnight(day, hour, mintues, second):
	
	hour_in_second = hour * 3600
	mintues_in_second = mintues * 60
	day_in_second = day * 86400
	seconds = hour_in_second + mintues_in_second + second  


	return seconds




day = input ("Enter your day \n") 
hours = int (input("enter your hour \n"))
mintues = int (input("enter your mintues \n"))
second = int(input("enter your seconds \n"))
result = seconds_since_midnight(day,hours,mintues,second)
print(result)
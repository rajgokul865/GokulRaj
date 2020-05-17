#############################################################################################################
#        Function for date validation    
#############################################################################################################

def date_validate(date,month,year):
	if(year>=1900 and year<=2020):
		if(month>=1 and month<=12):
			if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
				if(date>=1 and date <= 31):
					print "Date is valid"
				else:
					print "Invalid date"
			elif(month == 4 or month == 6 or month == 9 or month == 11):
				if(date >= 1 and date <= 30):
					print "Date is valid"
				else:
					print "Invalid date"
			elif(month == 2):
				if(date >= 1 and date <= 28):
					print "Date is valid"
				elif(date == 29):
					if(year%400 == 0 or year%4 == 0 and year%100 != 0):
						print "Date is valid"
					else:
						print "Invalid date"
				else:
					print "Invalid date"
		else:	
			print "Invalid Month"
	else:
		print "Invalid year"

###### Function end #########################################################################################


#############################################################################################################
#        Main    
#############################################################################################################

inputDate = raw_input("Enter the date in format 'dd/mm/yy' : ")
date,month,year = inputDate.split('/',3) 
date_validate(int(date),int(month),int(year))
	
		


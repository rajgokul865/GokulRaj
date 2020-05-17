import sys

SEATS = {1:'L',2:'M',3:'U',4:'L',5:'M',6:'U',7:'SL',8:'SU'}
TOTAL_NUM_SEATS = 72
NUM_ROWS = TOTAL_NUM_SEATS/len(SEATS)
choice = True

#############################################################################################################
#        Function for seat allocation    
#############################################################################################################

def seat_allocation(entry):
	if(int(entry)>0 and int(entry)<=72):
		for row in range(NUM_ROWS):
			for column in range(len(SEATS)):
				if(my_sub_list[row][column] == int(entry)):
					print "found!!!!"
					row_num = row + 1
					column_num = column + 1
					print "Seat allocated, ",SEATS[column_num]
					sys.exit(1)
	else:
		print "Invalid Entry!!!"

###### Function end #########################################################################################


#############################################################################################################
#        Main    
#############################################################################################################


mylist=list(range(1,TOTAL_NUM_SEATS + 1))
my_sub_list = [mylist[i:i + len(SEATS)] for i in xrange(0, len(mylist), len(SEATS))]

while choice:
	entry=raw_input("Enter the seat number:")
	seat_allocation(entry)
	choice=raw_input("do you want to continue:y/n")
	if choice == "y" or choice == "Y":
		choice = True
	else:
		choice = False

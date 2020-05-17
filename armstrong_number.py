import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('-n', '--Upperlimit',help='Input Upper Limit number')

args = parser.parse_args()

#############################################################################################################
#        Function for Armstrong number printing    
#############################################################################################################

def armstrong_num(num):
	sum_arm = 0
	num_digits = 0
	temp = num
	while temp != 0:
		num_digits = num_digits + 1
		temp = temp/10	
	temp=num
	while temp>0:
		digit=temp%10
		sum_arm = sum_arm + (digit**num_digits)
		temp=temp/10
	if num == sum_arm:
		print num
###### Function end #########################################################################################

#############################################################################################################
#        Main    
#############################################################################################################
if(not(args.Upperlimit)):
	sys.exit('ERROR:Need Upper limit as argument')
else:
	n = int(args.Upperlimit)
	for num in range (n+1):
		armstrong_num(num)

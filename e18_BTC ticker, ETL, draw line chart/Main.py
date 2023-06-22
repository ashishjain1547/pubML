# Python logger logs a row in the format "DEBUG:root:06/01/2018,02:07:03,1515184564,16350.0", 
# we are now removing the prefix "DEBUG:root:" from every row.

FILE_NAME = 'C:/Users/Ashish Jain/Desktop/BTC.csv'

def removeInlineHeaders():
	# Removes inline headers "Date,Time,USD/BTC" that appear in the middle of the CSV file every time the python script is restarted.
	import re
	f = open(FILE_NAME)
	raw = f.read()
	linesArr = re.split(r'\r?\n', raw)
	f.close()

	#Removing the file as it is now loaded in the 'linesArr' list.
	import os
	os.remove(FILE_NAME)

	out = open(FILE_NAME, 'a')
	for j in range(0, len(linesArr) - 1):
		if j != 0 and ("Date" in linesArr[j] or "None" in linesArr[j]):
			continue
		out.write(linesArr[j] + "\n")
	out.close()
	
def halveCSVFile():
	import re
	f = open(FILE_NAME)
	raw = f.read()
	linesArr = re.split(r'\r?\n', raw)
	f.close()

	#Removing the file as it is now loaded in the 'linesArr' list.
	import os
	os.remove(FILE_NAME)
	
	out = open(FILE_NAME, 'a')
	for j in range(0, len(linesArr) - 1):
		if j%2 == 0:
			out.write(linesArr[j] + "\n")
	out.close()

	
def getOneRowPerDate():
	import csv
	from datetime import datetime

	#with open(FILE_NAME) as file_obj:
	file_obj = open(FILE_NAME)
	
	reader = csv.DictReader(file_obj, delimiter=',')
	
	lastDate = ''
	# Getting the first 'Date'
	for line in reader:
		lastDate = line["Date"]
		break
	
	# Reading the 'reader' object (csv.DictReader) again now to write data
	linesArr = ['Date,USD/BTC']
	lastLine = ''
	for line in reader:
		if lastDate == line['Date']:
			lastLine = line
			continue
		else:
			linesArr.append(lastLine['Date'] + ',' + lastLine['USD/BTC'])
			lastLine = line
			lastDate = line['Date']
	
	# Appending the last line as well
	linesArr.append(line['Date'] + ',' + line['USD/BTC'])
	file_obj.close()
	
	# Writing to new file
	out = open(FILE_NAME + '.csv', 'w')
	for j in range(0, len(linesArr)):	
		out.write(linesArr[j] + "\n")
	out.close()
	
def main():
	removeInlineHeaders()
	
	print('Menu' + '\n1: Halve the file' + '\n2: Get data sampled by one row per date' + '\n3: Exit')
	selectedOption = input('Please enter your choise: ')
	
	while selectedOption == '1' or selectedOption == '2':	
		if selectedOption == '1':
			halveCSVFile()
			continueOrNot = input('Want to continue and halve the file (y/n)? Ans: ')
			while continueOrNot == 'y':
				halveCSVFile()
				continueOrNot = input('Want to continue and halve the file (y/n)? Ans: ')
		if selectedOption == '2':
			getOneRowPerDate()
		
		print('Menu' + '\n1: Halve the file' + '\n2: Get data sampled by one row per date' + '\n3: Exit')
		selectedOption = input('Please enter your choise: ')
	
main()
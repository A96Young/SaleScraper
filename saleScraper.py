from scanner import scrapTo
import datetime
import os

#set the year, month, and date in order to archive sale info
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
date = datetime.datetime.now()
year = str(date.year)
month = months[date.month-1]
day = str(date.day)

#define the final filepath
filepath = "cs459/Final/SaleInfo/"+year+"/"+month

#checks if the filepath exists already. If it doesn't, creates the path
try:
	if not os.path.exists(filepath):
		os.makedirs(filepath)
except OSError:
	print("Error creating directory. "+filepath)
os.chdir(filepath)

#creates a file named after the current day and passes it to the scraper
filename = day+".txt"

scrapTo(filepath, filename)

print("End of Program")
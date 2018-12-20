from lxml import html
import requests
import io
import os

#scrapTo definition puts the information into the final
def scrapTo(filepath, filename):
	#removes the files if exists, then creates a blank one
	#I only want one file of sales per day
	try:
		os.remove(filename)
		print("Removing existing file")
	except:
		print("File does not exist yet")
	print("Creating new file")
	
	try:
		output = open(filename, "w+")
	except:
		print("Error creating file")
		exit()
	print("The file %s/%s was opened successfully for output" % (filepath, filename))
	output.write("SaleScraper.py Results\n\n\n")
	output.close()
	
	#following code is used to initialize the page and find the number of pages(ie, the last page) the script will run through
	page="http://store.steampowered.com/search/?specials=1&page=1"
	site = requests.get(page)
	doc = html.fromstring(site.content)
	specials = doc.xpath('//div[@id="search_result_container"]')[0]
	last_page = specials.xpath('.//div[@class="search_pagination_right"]/a/text()')
	last = last_page[-2]
	last = last.strip("\r").strip("\n").strip("\t").strip("\xa0")
	
	#the outer while loop cycles through each page of deals grabbing each games information as it goes
	x=1
	while x <= int(last):
		page="http://store.steampowered.com/search/?specials=1&page="
		page+=str(x)
		site = requests.get(page)
		#print a progress report of the current page being scrapped
		print("Scraping: page",x,"of",last)
		doc = html.fromstring(site.content)
		games = doc.xpath('//div[@class="responsive_search_name_combined"]')
	
		#while loop is used to get each game that is on sale individually
		y=0
		while y < len(games):
			game = doc.xpath('//div[@class="responsive_search_name_combined"]')[y]
			#grabs each game individually in the sales element
			for all in game:
				discount = game.xpath('.//div[@class="col search_discount responsive_secondrow"]/span/text()')
				#only grabs the title and prices if the discount element is present
				if(discount):
					title = game.xpath('.//span[@class="title"]/text()')
					original_price = game.xpath('.//div[@class="col search_price discounted responsive_secondrow"]/span/strike/text()')
					current_price = game.xpath('.//div[@class="col search_price discounted responsive_secondrow"]/text()[position()=2]')
	
			#if the discount field is present, set all the information to strings, strip unwanted info, and the print the strings
			if(discount):
				discount = discount[0].strip("-").strip("%")
				
				titleStringToPrint = str(title[0])
				current_priceStringToPrint = "Current: " + str(current_price[0])
				original_priceStringToPrint = "Original:" + str(original_price[0])
				discountStringToPrint = "Discount: " + discount + "% off!"
				
				with open(filename, "a", encoding="utf-8") as output:
					output.write(titleStringToPrint)
					output.write("\n")
					output.write(current_priceStringToPrint)
					output.write("\n")
					output.write(original_priceStringToPrint)
					output.write("\n")
					output.write(discountStringToPrint)
					output.write("\n\n")
					output.close()
			y+=1
		x+=1
	#print the finished comment to alert users of teh progress
	print("Finished writing output to file")
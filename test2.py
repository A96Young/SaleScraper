from lxml import html
import requests
from decimal import Decimal

#following code is used to initialize the page and find the number of pages the script will run through
page="http://store.steampowered.com/search/?specials=1&page=28"
site = requests.get(page)
doc = html.fromstring(site.content)
specials = doc.xpath('//div[@id="search_result_container"]')[0]

titles = specials.xpath('.//span[@class="title"]/text()')
discounts = specials.xpath('//div[@class="col search_discount responsive_secondrow"]/span/text()')

print(page)
x=0
while x<len(titles):
	try:
		temp_discount = specials.xpath('//div[@class="col search_discount responsive_secondrow"]/span/text()')[x]
		if temp_discount:
			title = specials.xpath('.//span[@class="title"]/text()')[x]
			print(title)
			print(temp_discount)
	except:
		print("Error message 1")
	x+=1





	
	#loop to get discounts. If discount field is there, get the title and prices too
	#z=0
	#while z<len(discounts):
#		titles = specials.xpath('./span[@class="title"]/text()')[z]
#		original_price = specials.xpath('./div[@class="col search_price discounted responsive_secondrow"]/span/strike/text()')[z]
#		current_price = specials.xpath('./div[@class="col search_price discounted responsive_secondrow"]/text()[position()=2]')[z]
	#	discount = discounts[z]
	
#		original_price = [all.strip("$") for all in original_price]
#		current_price = [all.strip("$").strip("\t") for all in current_price]
	#	discount = discount.strip("-").strip("%")
	#	print(discount)
	#	z+=1
#	titles = specials.xpath('.//span[@class="title"]/text()')

from lxml import html
import requests
from decimal import Decimal

#following code is used to initialize the page and find the number of pages the script will run through
page="http://store.steampowered.com/search/?specials=1&page=1"
site = requests.get(page)
doc = html.fromstring(site.content)
specials = doc.xpath('//div[@id="search_result_container"]')[0]
last_page = specials.xpath('.//div[@class="search_pagination_right"]/a/text()')
last = last_page[-2]
last = last.strip("\r").strip("\n").strip("\t").strip("\xa0")

#Debug: print command to test the last page
#print(last)

x=1
while x <= int(last):
	page="http://store.steampowered.com/search/?specials=1&page="
	page+=str(x)
	site = requests.get(page)
	print(page)
	doc = html.fromstring(site.content)
	specials = doc.xpath('//div[@id="search_result_container"]')[0]
	discount_price_info = specials.xpath('//div[@class="col search_price_discount_combined responsive_secondrow"]')
	discounts = specials.xpath('//div[@class="col search_discount responsive_secondrow"]/span/text()')
	
	#loop to get discounts. If discount field is there, get the title and prices too
	z=0
	while z<len(discounts):
#		title = specials.xpath('./span[@class="title"]/text()')[z]
#		original_price = specials.xpath('./div[@class="col search_price discounted responsive_secondrow"]/span/strike/text()')[z]
#		current_price = specials.xpath('./div[@class="col search_price discounted responsive_secondrow"]/text()[position()=2]')[z]
		discount = discounts[z]
	
#		original_price = [all.strip("$") for all in original_price]
#		current_price = [all.strip("$").strip("\t") for all in current_price]
		discount = discount.strip("-").strip("%")
		print(discount)
		z+=1
#	titles = specials.xpath('.//span[@class="title"]/text()')
	x+=1
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
	exceptions = specials.xpath('.//div[@class="col search_discount responsive_secondrow"]/../following-sibling::span[@class="title"]/text()')
	titles = specials.xpath('.//span[@class="title"]/text()')
	original_price = specials.xpath('.//div[@class="col search_price discounted responsive_secondrow"]/span/strike/text()')
	current_price = specials.xpath('.//div[@class="col search_price discounted responsive_secondrow"]/text()[position()=2]')
	
	print("Exceptions: ",exceptions)
	y=0
	while y < len(titles):
		if(titles[y] == "Steam Controller"):
			del titles[y]
		y+=1
			
	original_price = [all.strip("$") for all in original_price]
	current_price = [all.strip("$").strip("\t") for all in current_price]
	
	print("Title:",titles)
	print("Original:",original_price)
	print("Current:",current_price)
	print("Length:",len(titles))
	
	i=0
	while i < len(titles):
		print(i)
		print(titles[i])
		print("Price: $", current_price[i])
		difference = Decimal(original_price[i]) - Decimal(current_price[i])
		print("You'll save $", difference, "from the original $", original_price[i], "!")
		print(i)
		print("")
		i+=1
	specials = []
	titles = []
	original_price = []
	current_price = []
	x+=1
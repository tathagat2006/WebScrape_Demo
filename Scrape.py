from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
# bs4 will parse the html text and urllib will grab the page itself.


my_url= 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

#now grab the webpage and download it ..
client=uReq(my_url)
page_html=client.read()
client.close()

 #call soup as function 

page_soup=soup(page_html,"html.parser")

 #grabbing each product.... it will retuen a dictionary which is named container by us.
container=page_soup.findAll("div",{"class":"item-container"})
 #checking the length of the container variable .. to see whether we are doing it correct or not.

# length=len(container)
 #call container[0] then save the html in a seperate file then use jsbeautifier to perfectly indent your html code.

 #

filename="products.csv"
f=open(filename,"w")
headers="brand,product_name,shipping\n"




for contain in container:
	brand = contain.div.div.a.img["title"]
	name = contain.findAll("a",{"class":"item-title"})
	title=name[0].text
	shipping_container = contain.findAll("li",{"class":"price-ship"})
	shipping = shipping_container[0].text.strip()

	print("brand : " + brand)
	print("title : " + title)
	print("shipping : " + shipping)

 #strip() function is used to remove white spaces and new line i.e. \r and \n
	f.write(brand + " , " + title.replace(",","|") + " , " + shipping + "\n")

f.close() 

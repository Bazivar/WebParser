from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen
from pdfrw import PdfReader, PdfWriter
import os

item_id = 'EVCP060D5IP00'


save_path = os.path.dirname(os.path.realpath(__file__)) + f'\RESULT\SE_files\{item_id}'

#getting the page
site = f"https://www.se.com/ru/ru/product/{item_id}/"
req = Request(site, headers={'User-Agent': 'Chrome/91.0'})
soup = BeautifulSoup(urlopen(req), features="html.parser")

#get the item short name
item_short_name = soup.find("title").get_text()[:-28].replace(' - ','').replace(item_id,'')  # get the item short name

# get the description
item_raw_left_desc = soup.find_all("th", class_="specifications-table__row-heading")
item_raw_right_desc = soup.find_all("td", class_="specifications-table__cell")
item_left_descr = []
item_right_descr = []
for i in range(len(item_raw_left_desc)):
    item_left_descr.append(item_raw_left_desc[i].get_text()+':')
    item_right_descr.append(item_raw_right_desc[i].get_text('; '))

#creating the HTML description
html_desc = ""
for i in range(len(item_right_descr)):
    html_desc =html_desc + "<li>" + item_left_descr[i] + " " + item_right_descr[i] +"</li>\n"

file_description = ("<html><head></head>\n" +
                    "<body>\n" +
                    "<div>" + item_short_name + "</div>\n"
                    "<div><br></div>\n"+
                    "<h3><b>ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ</b></h3>\n"+
                    "<div><br></div>" + "<div>\n" +
                    "<ul>\n" +
                    html_desc + "</ul></div></body></html>"
                    ).replace(' ;','')
#saving HTML description to a file
f = open(save_path+'-html.html', 'w', encoding='utf-8')
f.write(file_description)
f.close()


# get the item img files list
item_image_link = soup.find('img', class_='zoom__img sc-pes-media-gallery-zoom')['src']

# get the item_pdf:
item_pdf_link = f"https://www.se.com/ru/ru/product/download-pdf/{item_id}"

#saving the files:
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Chrome/91.0')]
urllib.request.install_opener(opener)
urllib.request.urlretrieve(item_pdf_link, save_path+"-pdf.pdf")
urllib.request.urlretrieve(item_image_link, save_path+"-png.png")

#setting the PDF file title
trailer = PdfReader(save_path+"-pdf.pdf")
trailer.Info.Title = item_id + " Описание " + item_short_name
PdfWriter(save_path+"-pdf.pdf", trailer=trailer).write()
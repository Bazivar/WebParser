from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen, urlretrieve
from pdfrw import PdfReader, PdfWriter
import os

#start page https://dlink.ru/ru/products/16/1721.html
#last page https://dlink.ru/ru/products/0/2554.html

def parce (site):
    req = Request(site, headers={'User-Agent': 'Chrome/91.0'})
    soup = BeautifulSoup(urlopen(req), features="html.parser")

    #getting the item ID
    item_id = soup.find("h2").getText()

    #setting the save path
    if '/' in item_id:
        raw_item_id = item_id.replace('/', '-')
    else:
        raw_item_id = item_id

    save_path = os.path.dirname(os.path.realpath(__file__)) + f"\RESULT\Dlink_files\{raw_item_id}"

    #getting the item short name
    item_short_name = soup.find("div", class_="description").getText()

    #getting the item image link
    item_image_link = "https://dlink.ru/" + soup.find("div", class_="product-images").find("img", src=True)["src"]

    #getting the item usage and benefits
    item_usage_desc = soup.find("div", class_="sub-content-block open").getText().split("\n")
    benefits  = ""
    for i in range(len(item_usage_desc)):
        if item_usage_desc[i]=="" or item_usage_desc[i]=="\r" or item_usage_desc[i]=="\t\xa0": continue
        else: benefits += "<li>" + item_usage_desc[i] +"\n"

    #gettingt the html description in a form of table
    item_description = soup.find("div", class_="sub-content-block table")

    #getting the PDF description link
    try:
        item_pdf_link = soup.find("div", class_="downloads-links").find("a", href=True)["href"]
    except:
        item_pdf_link = None

    # saving the img file
    urllib.request.urlretrieve(item_image_link, save_path + "-png.png")

    #saving the html file
    file_description = ("<html><head></head>\n" +
                                                "<body>\n" + "<div>" + item_short_name + "</div>\n"
                                                "<div>" + "<h3><b>НАЗНАЧЕНИЕ И ОСОБЕННОСТИ</b></h3>\n" + "<div><br></div>\n" +
                                                benefits + "</div>\n" +
                                                "<h3><b>ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ</b></h3>\n"+
                                                "<div><br></div>" + "<div>\n" +
                                                "<ul>\n" +
                                                str(item_description) + "</ul></div></body></html>"
                                                )

    #saving HTML description to a file
    f = open(save_path+'-html.html', 'w', encoding='utf-8')
    f.write(file_description)
    f.close()


    # saving the pdf file:
    if item_pdf_link == None:
        pass
    else:
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Chrome/91.0')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(item_pdf_link, save_path+"-pdf.pdf")
        #setting the PDF file title and author
        trailer = PdfReader(save_path+"-pdf.pdf")
        trailer.Info.Title = str(item_id) + " техническое описание"
        trailer.Info.Author = ''
        PdfWriter(save_path+"-pdf.pdf", trailer=trailer).write()

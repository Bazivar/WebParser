from googletrans import Translator
from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen
from pdfrw import PdfReader, PdfWriter
import os

translator = Translator()


def parce(site):
    #requesting the page
    req = Request(str(site), headers={'User-Agent': 'Chrome/91.0'})
    soup = BeautifulSoup(urlopen(req), features="html.parser")

    #getting the item id
    item_id = soup.find("span", class_="productMainTitle").getText()

    #setting the save path for files
    save_path = os.path.dirname(os.path.realpath(__file__)) + f"\RESULT\Mikrotik_files\{item_id}"

    #getting short description and translating it
    item_short_desc = soup.find("span", class_="productMainDescr").getText().replace("\n ","")
    item_short_desc = translator.translate(item_short_desc,src='en', dest='ru').text

    #getting usage and benefits descriptioon and translating it
    item_usage_desc = soup.find("div", class_="large-12 columns product-page").find("p").getText()
    item_usage_desc = translator.translate(item_usage_desc,src='en', dest='ru').text

    #getting the description, translating and converting it
    item_raw_description = soup.find_all("table", class_="table product-table")
    description = ""
    for i in item_raw_description:
        description += i.getText().replace('\n\n','').replace("Details","")
    item_raw_description = description.split("\n")
    i = 0
    item_description = ""
    while i < len(item_raw_description)-1:
        if item_raw_description[i] == "":
            i += 2
            continue
        else:
            item_description += "<li>" + item_raw_description[i] + " " + item_raw_description[i+1] + "\n"
            i+=2
    item_description = translator.translate(item_description,src='en', dest='ru').text

    #setting the file desctiption
    file_description = ("<html><head></head>\n" +
                                                            "<body>\n" + "<div>" + item_short_desc + "</div>\n" + "<div><br></div>\n" +
                                                            "<div>" + "<h3><b>НАЗНАЧЕНИЕ И ОСОБЕННОСТИ</b></h3>\n" + "<div><br></div>\n" +
                                                            item_usage_desc +"</div>\n" + "<div><br></div>\n" +
                                                            "<h3><b>ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ</b></h3>\n"+
                                                            "<div><br></div>" + "<div>\n" +
                                                            "<ul>\n" +
                                                            item_description + "</ul></div></body></html>"
                                                            )
    #saving html file
    f = open(save_path+'-html.html', 'w', encoding='utf-8')
    f.write(file_description)
    f.close()

    #getting the pdf link
    item_pdf_link = soup.find("a", class_="right button tiny radius")["href"]

    #saving the pdf file
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Chrome/91.0')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(item_pdf_link, save_path+"-pdf.pdf")
    #setting the PDF file title and author
    trailer = PdfReader(save_path+"-pdf.pdf")
    trailer.Info.Title = str(item_id) + " техническое описание"
    trailer.Info.Author = ''
    PdfWriter(save_path+"-pdf.pdf", trailer=trailer).write()

    #getting the image link
    item_image_link = soup.find("a", class_="product_image")["href"]

    # saving the img file
    urllib.request.urlretrieve(item_image_link, save_path + "-png.png")
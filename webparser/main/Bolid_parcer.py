from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen, urlretrieve
import re
from pdfrw import PdfReader, PdfWriter
import os

def parce (site):
    # getting the page
    req = Request(site, headers={'User-Agent': 'Chrome/91.0'})
    soup = BeautifulSoup(urlopen(req), features="html.parser")

    # getting the item id
    item_id = soup.find("var", style="display:none").getText()

    #setting the save path
    if '"' in item_id:
        raw_item_id = item_id.replace('"', '')
    elif '/' in item_id:
        raw_item_id = item_id.replace('/', '-')
    else:
        raw_item_id = item_id
    save_path = os.path.dirname(os.path.realpath(__file__)) + f"\RESULT\Bolid_files\{raw_item_id}"

    # getting the item short name
    item_short_name = soup.find("title").getText()

    # getting the item usage description
    meta = soup.find_all("meta")

    # item_usage_desc = str(meta[6]).replace('<meta content="', '').replace('" name="description"/>', '')
    item_usage_desc = soup.find("div",class_="new_fix_right").getText()

    #getting the image
    item_image_link = re.search(r'content="https://shop.bolid.ru/.+[pngj]{3}',str(meta)).group(0).replace('content="','')

    # getting the item benefits
    item_benefits = soup.find("div", class_="tabs_content active").getText()

    #getting the table of item description
    item_description_html = str(soup.find("div", id= "characteristics")).replace('<div class="tabs_content" data-r="1" id="characteristics">\n<div><table width="95%">','<table width="95%" border="1">').replace('</div>','')

    #getting the manual link
    item_manual_link_set = soup.find_all("a", href = True, class_="green")
    item_manual_link = None
    for i in item_manual_link_set:
        element = str(i)
        if "Руководство по эксплуатации"in element or "Руководство пользователя" in element or "Инструкция оператора" in element:
            item_manual_link = "https://bolid.ru" + i["href"]


    #creating the HTML description and description
    item_benefits = item_benefits.split("\n")
    benefits  = ""
    for i in range(len(item_benefits)):
        if item_benefits[i]=="":
            continue
        benefits += "<li>" + item_benefits[i] +"\n"
    benefits = "<h3><b>ОСОБЕННОСТИ</b></h3>\n" + "<div><br></div>\n" + benefits + "<div><br></div>\n"

    file_description = ("<html><head></head>\n" +
                                    "<body>\n" +
                                    "<div>" +
                                    item_short_name + "</div>\n"
                                    "<div><br></div>\n"+ "<h3><b>НАЗНАЧЕНИЕ</b></h3>\n"+
                                    item_usage_desc + benefits +
                                    "<h3><b>ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ</b></h3>\n"+
                                    "<div><br></div>" + "<div>\n" +
                                    "<ul>\n" +
                                    item_description_html + "</ul></div></body></html>"
                                    )
    #saving HTML description to a file
    f = open(save_path+'-html.html', 'w', encoding='utf-8')
    f.write(file_description)
    f.close()


    if item_manual_link == None:
        pass
    else:
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Chrome/91.0')]
        urllib.request.install_opener(opener)
        # setting the pdf path
        save_path_pdf = save_path + "-pdf.pdf"
        urllib.request.urlretrieve(item_manual_link, save_path_pdf)

        # setting the PDF file title and author
        trailer = PdfReader(save_path_pdf)
        trailer.Info.Title = str(item_short_name) + " руководство по эксплуатации"
        trailer.Info.Author = ''
        PdfWriter(save_path_pdf, trailer=trailer).write()

    #saving the image file
    urllib.request.urlretrieve(item_image_link, save_path+"-png.png")

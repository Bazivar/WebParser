from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen, urlretrieve
from pdfrw import PdfReader, PdfWriter
import os

def parce (site):
    req = Request(str(site), headers={'User-Agent': 'Chrome/91.0'})
    soup = BeautifulSoup(urlopen(req), features="html.parser")

    #getting item Id and short name
    item_h1 = soup.find("h1")
    item_id = item_h1.find("sup").getText()
    item_short_desc = item_h1.getText()

    save_path = os.path.dirname(os.path.realpath(__file__)) + f"\RESULT\\Ubiquiti_files\{item_id}"

    #getting the item usage description
    item_usage_desc = soup.find("p").getText()

    #getting item image link
    item_image_link = soup.find("div", class_= "item").find("a")["href"]
    if "http://www.ubnt.su/" not in item_image_link: item_image_link = "http://www.ubnt.su/" + item_image_link
    #saving image file
    urllib.request.urlretrieve(item_image_link, save_path + "-png.png")

    #getting the benefits
    benefits = soup.find("div", class_="tab-content").find_all('p')
    raw_benefits =""
    for i in range(len(benefits)):
        if i == 0:
            continue
        else:
            raw_benefits += benefits[i].getText()
    raw_benefits = raw_benefits.split("\n")
    item_benefits = ""
    for i in raw_benefits:
        if i =="": continue
        elif i=="   \r": continue
        elif i=="\r": continue
        else: item_benefits += "<li>" + i + "</li>" + "\n"

    #getting the item description
    try:
        description = soup.find("table", class_="tehinfo").find_all("td")
        item_description = "<ul>"
        i = 0
        while i != len(description):
            item_description += "<li>" + description[i].getText() + " " + description[i + 1].getText() + "</li>" + "\n"
            i += 2
        item_description += "</ul>"
    except:
        item_description = str(soup.find("div", class_="spisok"))

    if item_benefits != "": benefits = "<h3><b>ОСОБЕННОСТИ</b></h3>\n" + "<div><br></div>\n" + item_benefits
    else: benefits = ""

    file_description = ("<html><head></head>\n" +
                                                                "<body>\n" + "<div>" + item_short_desc + "</div>\n" + "<div><br></div>\n" +
                                                                "<div>" + "<h3><b>НАЗНАЧЕНИЕ</b></h3>\n" + "<div><br></div>\n" +
                                                                item_usage_desc +"</div>\n" + "<div><br></div>\n" +
                                                                benefits +
                                                                "<h3><b>ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ</b></h3>\n"+
                                                                "<div><br></div>" + "<div>\n" +
                                                                item_description + "</div></body></html>"
                                                                )
    #saving html file
    f = open(save_path+'-html.html', 'w', encoding='utf-8')
    f.write(file_description)
    f.close()

    try:
        #getting item pdf link
        item_pdf_link = "http://www.ubnt.su" + soup.find_all("a", class_="ssil")[2]["href"]
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Chrome/91.0')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(item_pdf_link, save_path+"-pdf.pdf")
        #setting the PDF file title and author
        trailer = PdfReader(save_path+"-pdf.pdf")
        trailer.Info.Title = str(item_id) + " техническое описание"
        trailer.Info.Author = ''
        PdfWriter(save_path+"-pdf.pdf", trailer=trailer).write()
    except: pass
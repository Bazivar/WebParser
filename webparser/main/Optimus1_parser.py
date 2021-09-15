from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen, urlretrieve
from pdfrw import PdfReader, PdfWriter
import re
import urllib.parse
import os


def parce(site):
    req = Request(site, headers={'User-Agent': 'Chrome/91.0'})
    soup = BeautifulSoup(urlopen(req), features="html.parser")

    item_short_desc = soup.find("h1").getText()
    item_partnumber = soup.find("span", class_="articleValue").getText()

    try:
        item_id = re.search(r"Optimus.+",item_short_desc).group(0).replace("Optimus ", '')
    except:
        item_id = item_partnumber


    save_path = os.path.dirname(os.path.realpath(__file__)) + f"\RESULT\Optimus_files\{item_partnumber}"

    item_image_link = "https://optimus-cctv.ru" + soup.find("div", class_='goodsLinkPhoto').find("a")["href"]
    item_image_link = item_image_link.replace('lib/image.php?get_image=', 'images/prev/')
    try:
        urllib.request.urlretrieve(item_image_link, save_path + "-png.png")
    except:
        item_image_link = urllib.parse.quote((item_image_link)).replace("https%3A", "https:")
        urllib.request.urlretrieve(item_image_link, save_path + "-png.png")

    item_pdf_links = soup.find_all("div", class_="col-12 col-sm mb-2 mb-sm-0")

    for item_pdf_link in item_pdf_links:
        filname = item_pdf_link.getText()
        item_pdf_link =  item_pdf_link.find('a', class_='file-item-link')['href']
        link = "https://optimus-cctv.ru" + urllib.parse.quote(item_pdf_link)
        try:
            urllib.request.urlretrieve(link, save_path + filname + '-pdf.pdf')
        except:
            continue
        # setting the PDF file title and author
        trailer = PdfReader(save_path + filname +'-pdf.pdf')
        trailer.Info.Title = item_short_desc + " " + filname
        trailer.Info.Author = ''
        PdfWriter(save_path + filname + '-pdf.pdf', trailer=trailer).write()


    item_benefits = soup.find("p").getText().split("\n")
    benefits = "<ul>\n"
    for i in range(len(item_benefits)):
        benefits += "<li>" + item_benefits[i] + "</li>" + "\n"
    benefits += "</ul>"

    item_left_description = soup.find_all("span", class_="featureName")
    item_right_description = soup.find_all("span", class_="featureValue text-break")
    item_description = []
    for i in range(len(item_right_description)):
        item_description.append(item_left_description[i].getText() + ": " + item_right_description[i].getText())

    html_desc = "<ul>\n"
    i = 0
    while i != len(item_description):
        html_desc = html_desc + "<li>" + item_description[i] + "</li>" + "\n"
        i += 1
    html_desc += "</ul>"

    file_description = ("<html><head></head>\n" +
                        "<body>\n" +
                        "<div>" +
                        item_short_desc + "</div>\n"
                                          "<div><br></div>\n" + "<div>\n" +
                        "<h3><b>ОСОБЕННОСТИ</b></h3>\n" + "</div>\n" +
                        "<div><br></div>\n" + "<div>\n" + benefits + "</div>\n<div>" +
                        "<div><br></div>\n" +
                        "<h3><b>ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ</b></h3>\n" + "</div>\n" +
                        "<div><br></div>" + "<div>\n" +
                        html_desc + "</div></body></html>"
                        )

    f = open(save_path + '-html.html', 'w', encoding='utf-8')
    f.write(file_description)
    f.close()
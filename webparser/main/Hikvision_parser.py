from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen
from pdfrw import PdfReader, PdfWriter
from googletrans import Translator
import urllib.parse
import os

translator = Translator()

def parce(site):
    req = Request(site, headers={'User-Agent': 'Chrome/91.0'})
    soup = BeautifulSoup(urlopen(req), features="html.parser")

    #getting the item id
    item_id = soup.find('h1').getText().replace('/', '_')
    save_path = os.path.dirname(os.path.realpath(__file__)) + f'\RESULT\Hikvision_files\{item_id}'

    #getting the item short description
    item_short_desc = soup.find('span', class_='prod_name-content').getText()
    item_short_desc = translator.translate(item_short_desc,src='en', dest='ru').text

    #setting the item benefits
    item_benefits = soup.find('ul', class_='product_description_item-list').getText()
    item_benefits = translator.translate(item_benefits,src='en', dest='ru').text

    benefits = item_benefits.split('\n')
    item_benefits = "<ul>\n"
    for element in benefits:
        item_benefits += '<li>' + element + "</li>\n"
    item_benefits += "</ul>\n"


    #getting the item description
    item_left_descriprion = soup.find_all('span', class_= 'tech-specs-items-description__title')
    item_right_description = soup.find_all('span', class_= 'tech-specs-items-description__title-details')
    item_description = '<ul>\n'
    for i in range(int(len(item_right_description)/2)):
        item_description += "<li>" + item_left_descriprion[i].getText() + ": " + item_right_description[i].getText() + '</li>\n'
    item_description = translator.translate(item_description,src='en', dest='ru').text

    #saving html file
    file_description = ("<html><head></head>\n" +
                                    "<body>\n" + "<div>" +
                                    item_short_desc + "</div>\n" + "<div><br></div>" + "<h3><b>ОСОБЕННОСТИ</b></h3>\n" +
                                    "</div>\n" + "<div><br></div>" + item_benefits +
                                    "<div><br></div>" + "<h3><b>ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ</b></h3>\n" + "</div>\n" +
                                    "<div><br></div>" + "<div>\n" +
                                    item_description + "</div></body></html>"
                                    )
    f = open(save_path + '-html.html', 'w', encoding='utf-8')
    f.write(file_description)
    f.close()


    #getting the item image:
    item_image_link = 'https://www.hikvision.com' + urllib.parse.quote(soup.find('meta', key = 'fess_image')['value'])
    urllib.request.urlretrieve(item_image_link, save_path + "-png.png")

    #getting the item pdf link
    try:
        try:
            item_pdf_link = 'https://www.hikvision.com' + soup.find('a', target='_blank')['data-href']
        except:
            item_pdf_link = 'https://www.hikvision.com' + soup.find('a', class_='card-space')['href']
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Chrome/91.0')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(item_pdf_link, save_path+"-pdf.pdf")
        #setting the PDF file title
        trailer = PdfReader(save_path+"-pdf.pdf")
        trailer.Info.Title = str(item_id) + " - техническое описание "
        PdfWriter(save_path+"-pdf.pdf", trailer=trailer).write()
    except:
        pass
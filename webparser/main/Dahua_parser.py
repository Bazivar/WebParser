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

    #getting the item ID
    item_id = 'DH-' + soup.find('title').getText().replace('/', '_')

    #setting the savepath of the files
    save_path = os.path.dirname(os.path.realpath(__file__)) + f'\RESULT\Dahua_files\{item_id}'

    #getting the item short description
    item_short_desc = soup.find('p', class_='text').getText()
    item_short_desc = translator.translate(item_short_desc, src='en', dest='ru').text

    #getting the item benefits:

    benefits = soup.find('div', class_='text-wrapper').getText().split('>')
    item_benefits = '<ul>\n'
    for i in range (len(benefits)):
        if i == 0 or i == 1: continue
        elif benefits[i] == '': continue
        elif benefits[i] == '\r': continue
        else: item_benefits += "<li>" + benefits[i].replace('\t','').replace('\r','').replace('>','') + '</li>\n'

    item_benefits += '</ul>'
    item_benefits = translator.translate(item_benefits,src='en', dest='ru').text.replace('\t','')


    #getting the item_description
    description = soup.find_all('tr')
    item_description = '<ul>\n'
    for i in range(int(len(description))-2):
         item_description += "<li>" + description[i].getText() + '</li>\n'
    item_description = translator.translate(item_description,src='en', dest='ru').text

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

    #getting the item image link
    item_image_link = soup.find('img', class_='prodcut-img')['src']
    urllib.request.urlretrieve(item_image_link, save_path + "-png.png")

    #getting the image pdf link
    item_pdfs = soup.find_all('td', class_='text-center')

    item_pdf_link = ''
    for element in item_pdfs:
        try:
            item_pdf_link = element.find('a')['href']
            break
        except: continue

    if item_pdf_link == '':
        pass
    else:
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Chrome/91.0')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(item_pdf_link, save_path + "-pdf.pdf")
        # setting the PDF file title
        trailer = PdfReader(save_path + "-pdf.pdf")
        trailer.Info.Title = str(item_id) + " - техническое описание "
        PdfWriter(save_path + "-pdf.pdf", trailer=trailer).write()
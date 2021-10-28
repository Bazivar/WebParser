from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from pdfrw import PdfReader, PdfWriter
from googletrans import Translator
import urllib.parse
import os

translator = Translator()

def parce (site):
    req = Request(site, headers={'User-Agent': 'Chrome/91.0'})
    soup = BeautifulSoup(urlopen(req), features="html.parser")

    #getting the item_id
    item_id = soup.find('div', class_='ptt').getText()

    #setting the save path
    save_path = os.path.dirname(os.path.realpath(__file__)) + f'\RESULT\\UNV_files\{item_id}'

    #getting the short pescription
    item_short_desc = soup.find('div', class_='ptt2 f_22').getText()
    item_short_desc = translator.translate(item_short_desc, src='en', dest='ru').text

    #getting item benefits
    benefits = soup.find('ul', class_='ul1').getText().split('•')
    item_benefits = '<ul>\n'
    for element in benefits:
        if element == '\n':continue
        else: item_benefits += "<li>" + element.replace('\n','') + ' </li>\n'
    item_benefits +='</ul>'

    item_benefits = translator.translate(item_benefits,src='en', dest='ru').text

    #getting the item description
    raw_description = soup.find_all('tr')
    item_description = '<ul>\n'
    for element in raw_description:
        if raw_description.index(element) in range (0, 2): continue
        else: item_description += "<li>" + element.getText(": ", strip=True)+ ' </li>\n'
    item_description +='</ul>'
    item_description = translator.translate(item_description,src='en', dest='ru').text

    #setting a html file description and saving it
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

    #getting and saving image file
    item_image_link = 'https://en.uniview.com/' + soup.find('div', class_='img1').find('img')['src']
    urllib.request.urlretrieve(item_image_link, save_path + "-png.png")

    #getting and saving pdf file
    try:
        item_pdf_link = 'https://en.uniview.com' + soup.find('div', class_='download').find('a')['href']
    except: item_pdf_link =''

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
        trailer.Info.Author = ''
        PdfWriter(save_path + "-pdf.pdf", trailer=trailer).write()


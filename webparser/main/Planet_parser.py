from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from googletrans import Translator
import urllib.parse
import os


translator = Translator()

def parse(site):

    req = Request(site, headers={'User-Agent': 'Chrome/91.0'})
    soup = BeautifulSoup(urlopen(req), features="html.parser")

    item_id = soup.find('h2', class_='h5 text-planet pt-2 m-0').getText()[4:].replace('/', '-')

    save_path = os.path.dirname(os.path.realpath(__file__)) + f'\RESULT\\Planet_files\{item_id}'

    item_short_desc = soup.find('h1', class_='h4').getText().replace('  ', '')
    item_short_desc = translator.translate(item_short_desc, src='en', dest='ru').text

    usage_desc = soup.find('div', class_='tab-pane fade pt-4').find_all('strong')

    item_usage_desc =''
    for element in usage_desc:
        item_usage_desc += ' ' + element.getText() + '. '
    item_usage_desc = translator.translate(item_usage_desc,src='en', dest='ru').text


    benefits = soup.find('div', class_='tab-pane fade show active pt-4').find_all('strong')
    item_benefits = '<ul>\n'
    for element in benefits:
        if len(element.getText().split(' ')) <3: continue
        else: item_benefits += "<li>" + element.getText() + ' </li>\n'
    item_benefits +='</ul>'
    item_benefits = translator.translate(item_benefits,src='en', dest='ru').text


    item_left_descr = soup.find_all('td', class_='align-middle', style = 'width:20%;min-width:150px; max-width:300px')[:-1]
    item_right_descr = soup.find_all('td', class_='')[:-1]


    item_description = '<ul>\n'
    for i in range (len(item_left_descr)):
       item_description += "<li> " + item_left_descr[i].getText() + ': ' + item_right_descr[i].getText("; ", strip=True) + ' </li>\n'
    item_description += '</ul>'
    item_description =  translator.translate(item_description, src='en', dest='ru').text

    file_description = ("<html><head></head>\n" +
                                                "<body>\n" + "<div>" +
                                                item_short_desc + "</div>\n" + "<div><br></div>" + "<h3><b>НАЗНАЧЕНИЕ</b></h3>\n" +
                                                "</div>\n" + "<div><br></div>" +
                                                item_usage_desc + "</div>\n" + "<div><br></div>" + "<h3><b>ОСОБЕННОСТИ</b></h3>\n" +
                                                "</div>\n" + "<div><br></div>" + item_benefits +
                                                "<div><br></div>" + "<h3><b>ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ</b></h3>\n" + "</div>\n" +
                                                "<div><br></div>" + "<div>\n" +
                                                item_description + "</div></body></html>"
                                                )
    f = open(save_path + '-html.html', 'w', encoding='utf-8')
    f.write(file_description)
    f.close()

    item_image_link = 'https://www.planet.com.tw' + soup.find('div', class_='gallery-modal-item')['src']
    urllib.request.urlretrieve(item_image_link, save_path + "-png.png")

    item_pdf_link = soup.find_all('a', target='_blank')
    files_number = soup.find_all('h5', class_='')
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Chrome/91.0')]
    urllib.request.install_opener(opener)

    for i in range (len(files_number)):
        urllib.request.urlretrieve('https://www.planet.com.tw' + item_pdf_link[i]['href'].replace(' ','%20'), save_path + '-' + files_number[i].getText()  + "-pdf.pdf")

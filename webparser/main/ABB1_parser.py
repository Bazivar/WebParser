from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen
import os
from googletrans import Translator

translator = Translator()



def parse (item_id):

    save_path = os.path.dirname(os.path.realpath(__file__)) + f'\RESULT\ABB_files\{item_id}'

    site = f"https://new.abb.com/products/{item_id}"
    req = Request(site, headers={'User-Agent': 'Chrome/91.0'})
    soup = BeautifulSoup(urlopen(req), features="html.parser")

    item_short_desc = soup.find('dd', itemprop='description').getText()
    item_short_desc = translator.translate(item_short_desc, src='en', dest='ru').text

    item_benefits = soup.find('dd', itemprop = 'longdescription').getText()
    item_benefits = translator.translate(item_benefits, src='en', dest='ru').text

    item_left_description = soup.find('div', class_='additional-information-section-wrapper').find_all('dt')
    item_right_description = soup.find('div', class_='additional-information-section-wrapper').find_all('dd')


    item_description = '<ul>\n'
    for i in range(len(item_left_description)):
        if 'Data Sheet, Technical Information' in item_left_description[i].getText(): continue
        if 'Instructions and Manuals' in item_left_description[i].getText(): continue
        if 'Dimension Diagram' in item_left_description[i].getText(): continue

        item_description += "<li>" + item_left_description[i].getText(": ", strip=True) + item_right_description[i].getText("; ", strip=True) + '</li>\n'
    item_description +='</ul>'
    item_description = translator.translate(item_description,src='en', dest='ru').text

    file_description = ("<html><head></head>\n" +
                                        "<body>\n" + "<div>" +
                                        item_short_desc + "</div>\n" + "<div><br></div>" + "<h3><b>НАЗНАЧЕНИЕ И ОСОБЕННОСТИ</b></h3>\n" +
                                        "</div>\n" + "<div><br></div>" + item_benefits +
                                        "<div><br></div>" + "<h3><b>ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ</b></h3>\n" + "</div>\n" +
                                        "<div><br></div>" + "<div>\n" +
                                        item_description + "</div></body></html>"
                                        )
    f = open(save_path + '-html.html', 'w', encoding='utf-8')
    f.write(file_description)
    f.close()

    item_image_link = soup.find('meta', itemprop='image')['content']
    urllib.request.urlretrieve(item_image_link, save_path + "-png.png")
from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen
import os
from googletrans import Translator
import openpyxl

translator = Translator()



def parce(a, b):
    a = int(a)
    b = int(b)
    # working with Excel:
    file = os.path.dirname(os.path.realpath(__file__)) + '\static\main\price\\abb_price.xlsx'
    wb = openpyxl.load_workbook(file)
    sheet = wb['1']
    for k in range(a,b+1):
        try: #avoiding exceptions in the program
            item_id = sheet[f'A{k}'].value #reading ID from the file
            save_path = os.path.dirname(os.path.realpath(__file__)) + f'\RESULT\ABB_files\{item_id}'

            site = f"https://new.abb.com/products/{item_id}"
            req = Request(site, headers={'User-Agent': 'Chrome/91.0'})
            soup = BeautifulSoup(urlopen(req), features="html.parser")

            item_short_desc = soup.find('dd', itemprop='description').getText()

            item_benefits = soup.find('dd', itemprop = 'longdescription').getText()

            item_left_description = soup.find('div', class_='additional-information-section-wrapper').find_all('dt')
            item_right_description = soup.find('div', class_='additional-information-section-wrapper').find_all('dd')


            item_description = '<ul>\n'
            for i in range(len(item_left_description)):
                if 'Data Sheet, Technical Information' in item_left_description[i].getText(): continue
                if 'Instructions and Manuals' in item_left_description[i].getText(): continue
                if 'Dimension Diagram' in item_left_description[i].getText(): continue

                item_description += "<li>" + item_left_description[i].getText(": ", strip=True) + item_right_description[i].getText("; ", strip=True) + '</li>\n'
            item_description +='</ul>'

            file_description = ("<html><head></head>\n" +
                                                "<body>\n" + "<div>" +
                                                item_short_desc + "</div>\n" + "<div><br></div>" + "<h3><b>НАЗНАЧЕНИЕ И ОСОБЕННОСТИ</b></h3>\n" +
                                                "</div>\n" + "<div><br></div>" + item_benefits +
                                                "<div><br></div>" + "<h3><b>ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ</b></h3>\n" + "</div>\n" +
                                                "<div><br></div>" + "<div>\n" +
                                                item_description + "</div></body></html>"
                                                )

            file_description = translator.translate(file_description, src='en', dest='ru').text

            f = open(save_path + '-html.html', 'w', encoding='utf-8')
            f.write(file_description)
            f.close()

            item_image_link = soup.find('meta', itemprop='image')['content']
            urllib.request.urlretrieve(item_image_link, save_path + "-png.png")
            sheet[f'F{k}'] = "Успешно"
        except:
            sheet[f'F{k}'] = "Ошибка"
            continue

    wb.save(file)
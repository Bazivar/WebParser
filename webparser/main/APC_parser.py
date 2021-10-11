from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.parse
import os


def parse (item_id):

    save_path = os.path.dirname(os.path.realpath(__file__)) + f'\RESULT\APC_files\{item_id}'

    site = f'https://www.apc.com/shop/by/ru/products/P-{item_id}'

    req = Request(site, headers={'User-Agent': 'Chrome/91.0'})
    soup = BeautifulSoup(urlopen(req), features="html.parser")

    item_short_desc = soup.find('title').getText()

    item_benefits = str(soup.find('ul', class_='product-description__text-section'))


    tech_descr = soup.find('div', id='technical_specification')
    item_left_desc = tech_descr.find_all('strong', class_='technical-content-block__category')
    item_right_desc = tech_descr.find_all('div', class_='technical-content-block__value')

    item_description = '<ul>\n'
    for i in range (len(item_left_desc)):
        if 'Время автономной работы' in item_left_desc[i].getText() or 'Эффективность' in item_left_desc[i].getText():continue
        if 'См. на вкладке' in item_right_desc[i].getText():continue
        item_description += "<li>" + item_left_desc[i].getText() + ': ' + item_right_desc[i].getText().replace('\n','') + '</li>\n'
    item_description +='</ul>'

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

    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Chrome/91.0')]
    urllib.request.install_opener(opener)
    item_image_link = soup.find('img', class_='product-description__main-block__image')['src']
    urllib.request.urlretrieve(item_image_link, save_path + "-png.png")
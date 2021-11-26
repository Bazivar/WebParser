from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from pdfrw import PdfReader, PdfWriter
import urllib.parse
import os

def parse (site):
    req = Request(site, headers={'User-Agent': 'Chrome/91.0'})
    soup = BeautifulSoup(urlopen(req), features="html.parser")

    item_id = soup.find('meta', content = True, itemprop = 'sku')['content']

    save_path = os.path.dirname(os.path.realpath(__file__)) + f'\RESULT\\CMO_files\{item_id}'

    item_short_desc = soup.find('meta', content = True, property = "og:title")['content']

    text_description = soup.find('div', class_='tab-content', id='tab-1').getText(' ', strip=True).split('. ')
    item_benefits = text_description[1:]
    item_usage_desc = text_description[0]

    file_benefits = '<ul>\n'
    for i in range (len (item_benefits)):
        file_benefits += "<li>" + item_benefits[i] + ' </li>\n'
    file_benefits += '</ul>\n'

    item_description = soup.find('table', class_='table-articles-1')

    item_options = soup.find_all('div', class_='col-sm-10')

    if item_options == []: file_options = "<div><br></div>"
    else:
        file_options = "<div><br></div>" + "<h3><b>ОПЦИИ</b></h3>\n" + "</div>\n" + "<div><br></div>" + "<div>\n" + '<ul>\n '
        for i in range (len (item_options)):
            file_options += "<li>" + item_options[i].getText(strip=True) + ' </li>\n'
        file_options += '</ul>\n'


    file_description = ("<html><head></head>\n" +
                                                "<body>\n" + "<div>" +
                                                item_short_desc + "</div>\n" + "<div><br></div>" + "<h3><b>НАЗНАЧЕНИЕ</b></h3>\n" +
                                                "</div>\n" + "<div><br></div>" + item_usage_desc +
                                                "</div>\n" + "<div><br></div>" + "<h3><b>ОСОБЕННОСТИ</b></h3>\n" +
                                                "</div>\n" + "<div><br></div>" + file_benefits +
                                                "<div><br></div>" + "<h3><b>ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ</b></h3>\n" + "</div>\n" +
                                                "<div><br></div>" + "<div>\n" +
                                                str(item_description) + file_options + "</div></body></html>"
                                                )
    f = open(save_path + '-html.html', 'w', encoding='utf-8')
    f.write(file_description)
    f.close()

    item_image_link = soup.find('meta', content = True, property = 'og:image')['content']
    urllib.request.urlretrieve(item_image_link, save_path + "-png.png")

    item_pdf_link = 'https://www.cmo.ru/' + soup.find('a', class_='file-type-pdf passport')['href'].replace(' ', '%20')

    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Chrome/91.0')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(item_pdf_link, save_path + "-pdf.pdf")
    # setting the PDF file title
    trailer = PdfReader(save_path + "-pdf.pdf")
    trailer.Info.Title = str(item_id) + " - паспорт производителя."
    trailer.Info.Author = ''
    PdfWriter(save_path + "-pdf.pdf", trailer=trailer).write()
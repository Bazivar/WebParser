from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen
from pdfrw import PdfReader, PdfWriter
import os

def parce (item_id):

    #setting the savepath
    item_id = item_id.replace('/','_')
    save_path = os.path.dirname(os.path.realpath(__file__)) + f'\RESULT\Wago_files\{item_id}'

    #setting the site and requesting it's page
    site = f"https://www.wago.com/ru/0/0/p/{item_id}"
    req = Request(site, headers={'User-Agent': 'Chrome/91.0'})
    soup = BeautifulSoup(urlopen(req), features="html.parser")

    #getting the item short description
    item_short_desc = soup.find('h1', class_='wg-product-title js-wg-quick-add-product-to-cart-name').getText().replace('\t','')

    #getting the item image link and saving it
    item_image_link = 'https://www.wago.com/' + soup.find('img', class_= 'is-zoomable')['data-src']
    urllib.request.urlretrieve(item_image_link, save_path + "-png.png")

    #getting the item usage description
    try:
        item_usage_desc = soup.find('div', class_='wg-product-desc__body').getText().replace('\t','')
        item_usage_desc =  "<div><br></div>" + "<h3><b>НАЗНАЧЕНИЕ И ОСОБЕННОСТИ</b></h3>\n" + "</div>\n" + "<div><br></div>" + item_usage_desc
    except:
        item_usage_desc = ""
    #getting the item description and removing the script tag
    item_descr_str = str(soup.find('script', id='template-product-tab-container'))[557:-9]

    #making a parcing process again to extract the description
    item_descr_str = BeautifulSoup(item_descr_str, features="html.parser")

    #getting the description
    desc = item_descr_str.find_all("tr", class_="")

    #extracting the description
    item_description = "<ul>\n"
    for i in range(len(desc)):
        item_description += '<li>' + desc[i].getText().replace('\n','').replace('\t',' ') + "</li>\n"
    item_description += "</ul>\n"

    #setting up the HTML-description ang saving the file
    file_description = ("<html><head></head>\n" +
                            "<body>\n" + "<div>" +
                            item_short_desc + "</div>\n" + item_usage_desc +
                            "<div><br></div>" + "<h3><b>ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ</b></h3>\n" + "</div>\n" +
                                        "<div><br></div>" + "<div>\n" +
                                        item_description + "</div></body></html>"
                                        )
    f = open(save_path + '-html.html', 'w', encoding='utf-8')
    f.write(file_description)
    f.close()

    item_pdf_link = f"https://www.wago.com/ru/products/datasheets/DataSheet.pdf?product={item_id}&lang=ru"
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Chrome/91.0')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(item_pdf_link, save_path+"-pdf.pdf")
    #setting the PDF file title
    trailer = PdfReader(save_path+"-pdf.pdf")
    trailer.Info.Title = str(item_id) + " " + item_short_desc + " Описание "
    PdfWriter(save_path+"-pdf.pdf", trailer=trailer).write()
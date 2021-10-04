from bs4 import BeautifulSoup
import urllib
from urllib.request import Request
from selenium import webdriver
import openpyxl
import os


def parce (a, b):
    file = os.path.dirname(os.path.realpath(__file__)) + '\static\main\price\phoenix_price.xlsx'
    wb = openpyxl.load_workbook(filename=file)
    sheet = wb['List']

    a = int(a)
    b = int(b)

    for k in range(a, b + 1):
        item_id = sheet[f'A{k}'].value
        # checking if we've got the ID and not the empty value
        if item_id == None:
            continue

        save_path = os.path.dirname(os.path.realpath(__file__)) + f"\RESULT\Phoenix_files\{item_id}"

        try:
            #getting page 1
            n = 1
            options = webdriver.ChromeOptions()
            options.add_argument("'User-Agent'")
            browser = webdriver.Chrome(options=options)
            site = f"https://www.phoenixcontact.com/online/portal/ru?uri=pxc-oc-itemdetail:pid={item_id}&library=rupl&tab={n}"
            browser.get(site)
            generated_html = browser.page_source
            soup = BeautifulSoup(generated_html, features="html.parser")

            #getting item short description
            item_short_desc = item_id + ' ' + soup.find("span", itemprop = 'title').getText().replace(item_id, '')[:-3]

            #getting item usage
            item_usage_desc = soup.find_all('p', class_=False, href = False)[1].getText()

            #getting the item add description
            item_left_add_descr = soup.find_all('th')
            item_right_add_descr = soup.find_all('td', class_=False)
            item_add_description = ""
            for i in range(len(item_left_add_descr)):
                item_add_description += '<li>' + item_left_add_descr[i].getText().replace('\n', '') + " " + item_right_add_descr[
                    i].getText().replace('\n', '')
                item_add_description += "</li>\n"


            #getting item benefits
            if soup.find("ul", class_="pxc-benefit") == None:
                item_benefits = "<div><br></div>\n"
            else:
                item_benefits = "<div>\n" +"<h3><b>ОСОБЕННОСТИ</b></h3>\n" + "</div>\n" + "<div><br></div>\n" + "<div>\n" +\
                                str(soup.find("ul", class_="pxc-benefit")).replace('<ul class="pxc-benefit">','<ul>') + "</div>\n" +\
                                "<div><br></div>\n"



            #getting item image link and saving the image
            item_image_link = soup.find('img', class_='pxc-img')['src'].replace('-B148','-B408')
            urllib.request.urlretrieve(item_image_link, save_path + "-png.png")

            #getting page 2
            n = 2
            site = f"https://www.phoenixcontact.com/online/portal/ru?uri=pxc-oc-itemdetail:pid={item_id}&library=rupl&tab={n}"
            browser.get(site)
            generated_html = browser.page_source
            soup = BeautifulSoup(generated_html, features="html.parser")
            browser.quit()

            item_left_descr = soup.find_all('th')
            item_right_descr = soup.find_all('td', class_=False)

            item_description = "<ul>\n"

            for i in range(len(item_left_descr)):
                if item_left_descr[i].getText()== "\n":
                    item_description = item_description[:-5]
                    item_description += ", " + item_right_descr[i].getText().replace('\n','')
                else:
                    item_description +='<li>' + item_left_descr[i].getText().replace('\n','') + " " + item_right_descr[i].getText().replace('\n','')
                item_description +="</li>\n"
            item_description +=item_add_description + "</ul>\n"

            #saving the description into html
            file_description = ("<html><head></head>\n" +
                                "<body>\n" + "<div>" +
                                item_short_desc + "</div>\n" + "<div><br></div>" +
                                "<h3><b>НАЗНАЧЕНИЕ</b></h3>\n" +  "</div>\n" + "<div><br></div>" + item_usage_desc +
                                "<div><br></div>" + item_benefits +
                                            "<h3><b>ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ</b></h3>\n" + "</div>\n" +
                                            "<div><br></div>" + "<div>\n" +
                                            item_description + "</div></body></html>"
                                            )
            f = open(save_path + '-html.html', 'w', encoding='utf-8')
            f.write(file_description)
            f.close()
            sheet[f'L{k}'].value = "Данные собраны"
        except:
            sheet[f'L{k}'].value = "Ошибка"
            continue
    wb.save(file)
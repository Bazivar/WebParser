from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen, urlretrieve
import re
import openpyxl
from pdfrw import PdfReader, PdfWriter
import os


def parce (a,b):
    a = int(a)
    b = int(b)
    # working with Excel:
    file = os.path.dirname(os.path.realpath(__file__)) + '\static\main\price\dkc_price.xlsx'
    wb = openpyxl.load_workbook(filename=file)
    sheet = wb['1']

    for k in range (a,b+1):
        item_id = sheet[f'F{k}'].value #reading ID from the file
        #checking if we've got the ID and not the empty value
        if item_id == None:
            continue

        #setting the save path
        save_path = os.path.dirname(os.path.realpath(__file__)) + f'\RESULT\DKC_files\{item_id}'

        try:
            #getting the page
            site = f"https://www.dkc.ru/ru/catalog/0/{item_id}/"
            req = Request(site, headers={'User-Agent': 'Chrome/91.0'})
            soup = BeautifulSoup(urlopen(req), features="html.parser")

            #getting the item short name
            try:
                item_short_name = soup.find("h1", class_="catalogItem__title").get_text()
            except:
                continue

            #getting image link
            item_image_link = "https://www.dkc.ru" + re.search(r'/upload/iblock/.+[pngj]{3}', str(soup)).group(0)

            #getting the item usage description
            try:
                item_usage_desc = soup.find("div", class_="catalogsDetail__descText").get_text()
                item_usage_desc = item_usage_desc.replace("          ", '')
                item_usage_desc = item_usage_desc.replace("\n", '')
            except:
                item_usage_desc = None
            item_description = str(soup.find_all("table", class_="charsTable__table"))
            item_description = re.findall(r">\n[\s]+(.+)</td>", item_description)
            for i in range(len(item_description)):
                item_description[i] = item_description[i].replace("                                                                                                                                                    ","")

            #getting the pdf link
            try:
                item_pdf_link = "https://www.dkc.ru" + re.search(r'(/upload/iblock/.+\.pdf)', str(soup)).group(0)
            except:
                item_pdf_link = None

            #creating the HTML description and description
            html_desc = ""
            description = ""
            i = 0
            while i != len(item_description):
                html_desc =html_desc + "<li>" + item_description[i] + " " + item_description[i+1] +"\n"
                description = description + " " + item_description[i] + " " + item_description[i+1] +"\n"
                i +=2

            if item_short_name == None:
                desc = ""
            else:
                desc = item_short_name
            if item_usage_desc == None:
                usage = ""
            else:
                usage = "<h3><b>???????????????????? ?? ??????????????????????</b></h3>\n" + "<div><br></div>\n" + item_usage_desc + "<div><br></div>\n"

            file_description = ("<html><head></head>\n" +
                                            "<body>\n" +
                                            "<div>" + desc + "</div>\n"
                                            "<div><br></div>\n"+
                                            usage +
                                            "<h3><b>?????????????????????? ????????????????????????????</b></h3>\n"+
                                            "<div><br></div>" + "<div>\n" +
                                            "<ul>\n" +
                                            html_desc + "</ul></div></body></html>"
                                            )

            #saving HTML description to a file
            f = open(save_path+'-html.html', 'w', encoding='utf-8')
            f.write(file_description)
            f.close()

            # saving the pdf file:
            if item_pdf_link == None:
                pass
            else:
                opener = urllib.request.build_opener()
                opener.addheaders = [('User-agent', 'Chrome/91.0')]
                urllib.request.install_opener(opener)
                urllib.request.urlretrieve(item_pdf_link, save_path+"-pdf.pdf")
                #setting the PDF file title
                trailer = PdfReader(save_path+"-pdf.pdf")
                trailer.Info.Title = str(item_id) + " ???????????????? " + item_short_name
                PdfWriter(save_path+"-pdf.pdf", trailer=trailer).write()

            #saving the img file
            urllib.request.urlretrieve(item_image_link, save_path+"-png.png")

            #filling the Ecxel sheet
            if item_pdf_link != None:
                sheet[f'L{k}'] = item_pdf_link
            sheet[f'M{k}'] = item_image_link
            sheet[f'N{k}'] = item_usage_desc
            sheet[f'O{k}'] = str(description)
        except:
            sheet[f'O{k}'] = "????????????"
            continue
    wb.save(file)
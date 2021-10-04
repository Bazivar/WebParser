from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen
import re
import openpyxl
from pdfrw import PdfReader, PdfWriter
import os

def parce (a,b):
    file = os.path.dirname(os.path.realpath(__file__)) + '\static\main\price\itk_price.xlsx'
    wb = openpyxl.load_workbook(filename=file)
    sheet = wb['Прайс']

    a = int(a)
    b = int(b)

    for k in range(a, b+1):
        item_id = sheet[f'A{k}'].value
        if item_id == None:
            continue

        #setting the savign path
        save_path = os.path.dirname(os.path.realpath(__file__)) + f'\RESULT\ITK_files\{item_id}'

        #getting the short name

        item_short_name = sheet[f'B{k}'].value
        try:
            # getting the page
            site = f"https://www.itk-group.ru/produktsiya/catalog/?page=detail&article={item_id}"
            req = Request(site, headers={'User-Agent': 'Chrome/91.0'})
            soup = BeautifulSoup(urlopen(req), features="html.parser")
            strsoup = str(soup)

            # getting the image link

            item_image_link = "https://www.itk-group.ru" + re.search(r'/upload/iek.prodcat/file/.+[pngj]{3}', strsoup).group(0)
            item_image_link = item_image_link[:117]

            # getting the usage
            item_usage_desc = soup.find("div",
                                    style="border-top: 1px solid #76d750;border-bottom: 1px solid #76d750;padding: 15px 0; margin: 15px 0; white-space: pre-line;").getText()

            # getting the benefits
            item_benefits = soup.find("p", style="white-space: pre-line;").getText()

            # getiing description
            item_description = str(soup.find_all("td", style="padding: 5px;"))
            item_left_description = re.findall(r'<strong>(.+)</strong>', item_description)
            item_right_description = re.findall(r'(\t[\s\d\w,\.:/-]+)\n', item_description)
            item_description = []
            for i in range(len(item_right_description)):
                item_right_description[i] = item_right_description[i].replace("									", "")
                item_description.append(item_left_description[i] + " " + item_right_description[i])


            # getting the pdf link of passport
            try:
                item_passport_pdf_link = "https://www.itk-group.ru" + re.search(
                    r'title="Паспорт"><a href="(/local/components/iek/prodcat\.catalog\.detail/download\.php\?hash=[\w\d]+)',
                    strsoup).group(0)
                item_passport_pdf_link = item_passport_pdf_link.replace('title="Паспорт"><a href="', '')
            except:
                item_passport_pdf_link = None

            # getting the installation manual
            try:
                item_install_manual_pdf_link = "https://www.itk-group.ru" + re.search(
                    r'title="Руководство По Монтажу"><a href="(/local/components/iek/prodcat\.catalog\.detail/download\.php\?hash=[\w\d]+)',
                    strsoup).group(0)
                item_install_manual_pdf_link = item_install_manual_pdf_link.replace('title="Руководство По Монтажу"><a href="',
                                                                                    '')
            except:
                item_install_manual_pdf_link = None

            # getting the manual
            try:
                item_manual_pdf_link = "https://www.itk-group.ru" + re.search(
                    r'title="Руководство По Эксплуатации"><a href="(/local/components/iek/prodcat\.catalog\.detail/download\.php\?hash=[\w\d]+)',
                    strsoup).group(0)
                item_manual_pdf_link = item_manual_pdf_link.replace('title="Руководство По Эксплуатации"><a href="',
                                                                                    '')
            except:
                item_manual_pdf_link = None


            #creating the HTML description and description
            html_desc = ""
            description = ""
            i = 0
            while i != len(item_description):
                html_desc = html_desc + "<li>" + item_description[i] +"\n"
                description = description + " " + item_description[i] +"\n"
                i +=1

            if item_short_name == None:
                desc = ""
            else:
                desc = item_short_name
            if item_usage_desc == None:
                usage = ""
            else:
                usage = "<h3><b>НАЗНАЧЕНИЕ</b></h3>\n" + "<div><br></div>\n" + item_usage_desc + "<div><br></div>\n"
            if item_benefits == None:
                benefits = ""
            else:
                item_benefits = item_benefits.split("\n")
                benefits  = ""
                for i in range(len(item_benefits)):
                    benefits += "<li>" + item_benefits[i] +"\n"
                benefits = "<h3><b>ОСОБЕННОСТИ</b></h3>\n" + "<div><br></div>\n" + benefits + "<div><br></div>\n"

            file_description = ("<html><head></head>\n" +
                                            "<body>\n" +
                                            "<div>" +
                                            desc + "</div>\n"
                                            "<div><br></div>\n"+
                                            usage + benefits +
                                            "<h3><b>ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ</b></h3>\n"+
                                            "<div><br></div>" + "<div>\n" +
                                            "<ul>\n" +
                                            html_desc + "</ul></div></body></html>"
                                            )

            #saving HTML description to a file
            f = open(save_path+'-html.html', 'w', encoding='utf-8')
            f.write(file_description)
            f.close()

            # saving the 1st pdf file:
            if item_passport_pdf_link == None:
                pass
            else:
                opener = urllib.request.build_opener()
                opener.addheaders = [('User-agent', 'Chrome/91.0')]
                urllib.request.install_opener(opener)
                #setting the pdf path
                save_path_pdf = save_path+"-pdf.pdf"
                urllib.request.urlretrieve(item_passport_pdf_link, save_path_pdf)

                #setting the PDF file title and author
                trailer = PdfReader(save_path_pdf)
                trailer.Info.Title = str(item_id) + " паспорт"
                trailer.Info.Author = ''
                PdfWriter(save_path_pdf, trailer=trailer).write()

            # saving the 2nd pdf file:
            if item_install_manual_pdf_link == None:
                pass
            else:
                opener = urllib.request.build_opener()
                opener.addheaders = [('User-agent', 'Chrome/91.0')]
                urllib.request.install_opener(opener)
                # setting the pdf path
                if item_passport_pdf_link == None:
                    save_path_pdf = save_path+"-pdf.pdf"
                else:
                    save_path_pdf = f"RESULT/ITK_files/2nd_pdf/{item_id}-pdf.pdf"
                urllib.request.urlretrieve(item_install_manual_pdf_link, save_path_pdf)
                #setting the PDF file title and author
                trailer = PdfReader(save_path_pdf)
                trailer.Info.Title = str(item_id) + " Руководство по монтажу"
                trailer.Info.Author = ''
                PdfWriter(save_path_pdf, trailer=trailer).write()

            # saving the 3rd pdf file

            if item_manual_pdf_link == None:
                pass
            else:
                opener = urllib.request.build_opener()
                opener.addheaders = [('User-agent', 'Chrome/91.0')]
                urllib.request.install_opener(opener)
                # setting the pdf path
                if item_passport_pdf_link == None and item_install_manual_pdf_link == None:
                    save_path_pdf = f"RESULT/ITK_files/{item_id}-pdf.pdf"
                elif item_passport_pdf_link == None and item_install_manual_pdf_link != None:
                    save_path_pdf = f"RESULT/ITK_files/2nd_pdf/{item_id}-pdf.pdf"
                else:
                    save_path_pdf = f"RESULT/ITK_files/3rd_pdf/{item_id}-pdf.pdf"
                urllib.request.urlretrieve(item_manual_pdf_link, save_path_pdf)
                #setting the PDF file title and author
                trailer = PdfReader(save_path_pdf)
                trailer.Info.Title = str(item_id) + " Руководство по эксплуатации"
                trailer.Info.Author = ''
                PdfWriter(save_path_pdf, trailer=trailer).write()

            #saving the img file
            urllib.request.urlretrieve(item_image_link, save_path+"-png.png")

            #putting the info into Excel Sheet
            if item_passport_pdf_link != None:
                sheet[f'R{k}'] = item_passport_pdf_link
            if item_install_manual_pdf_link != None:
                 sheet[f'S{k}'] = item_install_manual_pdf_link
            if item_manual_pdf_link != None:
                sheet[f'T{k}'] = item_manual_pdf_link
            sheet[f'U{k}'] = item_image_link
            sheet[f'V{k}'] = item_usage_desc
            sheet[f'W{k}'] = str(item_benefits)
            sheet[f'X{k}'] = str(description)
        except:
            sheet[f'V{k}'] = "Ошибка"
            continue
    wb.save(file)
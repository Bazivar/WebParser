from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen
from pdfrw import PdfReader, PdfWriter
import os


def parce(item_id):
        save_path = os.path.dirname(os.path.realpath(__file__)) + f"\RESULT\Rittal_files\{item_id}"
        site = f"https://www.rittal.com/ru-ru/product/show/variantdetail.action?categoryPath=/0/0/0/0/0/0/0&productID={item_id}"
        req = Request(site, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'})
        soup = BeautifulSoup(urlopen(req), features="html.parser")

        # getting item short name
        item_short_desc = soup.find("title").getText()

        # getting usage description
        item_usage_desc = soup.find("meta", lang="ru")["content"]

        # getting the desctiption
        item_left_desc = soup.find_all("th", width="25%")
        item_right_desc = soup.find_all("td", width="75%")
        item_description = "<ul>"
        for i in range(len(item_left_desc)):
            item_description += "<li>" + item_left_desc[i].getText() + " " + item_right_desc[i].getText().replace("\t",
                                                                                                                  "").replace(
                "\n", "") + "</li>" + "\n"
            if "Описание" in item_left_desc[i + 1].getText(): break
        item_description += "</ul>"

        file_description = ("<html><head></head>\n" +
                            "<body>\n" + "<div>" + item_short_desc + "</div>\n" + "<div><br></div>\n" +
                            "<div>" + "<h3><b>НАЗНАЧЕНИЕ</b></h3>\n" + "<div><br></div>\n" +
                            item_usage_desc + "</div>\n" + "<div><br></div>\n" +
                            "<h3><b>ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ</b></h3>\n" +
                            "<div><br></div>" + "<div>\n" +
                            item_description + "</div></body></html>"
                            )

        f = open(save_path + '-html.html', 'w', encoding='utf-8')
        f.write(file_description)
        f.close()

        # getting and saving item image
        item_image_link = "https:" + soup.find("img", class_="LoadImg")["src"]
        urllib.request.urlretrieve(item_image_link, save_path + "-png.png")

        # getting and saving pdf
        item_pdf_link = "https://www.rittal.com" + soup.find("a", class_="Button SizeM LinkPDF")["href"]
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Chrome/91.0')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(item_pdf_link, save_path + "-pdf.pdf")
        # setting the PDF file title and author
        trailer = PdfReader(save_path + "-pdf.pdf")
        trailer.Info.Title = str(item_short_desc) + " техническое описание"
        trailer.Info.Author = ''
        PdfWriter(save_path + "-pdf.pdf", trailer=trailer).write()
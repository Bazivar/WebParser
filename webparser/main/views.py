from django.shortcuts import render
from .forms import ArticlesForm, NumbersForm


from .SE1_parser import parce as se1
from .DKC1_parser import parce as dkc1
from .Bolid_parcer import parce as bolid1
from .Dahua_parser import parce as dahua1
from .IEK1_parcer import parce as iek1
from .ITK1_parcer import parce as itk1
from .Optimus1_parser import parce as optimus1
from .Phoenix1_parser import parce as phoenix1
from .Rittal1_parser import parce as rittal1
from .Wago1_parser import parce as wago1
from .Dlink1_parcer import parce as dlink1
from .Hikvision_parser import parce as hikvision1
from .UNV_parser import parce as unv1
from .Mikrotik_parcer import parce as mikrotik1
from .Ubiquiti_parser import parce as ubiquiti1
from .APC_parser import parse as apc1
from .Planet_parser import parse as planet1
from .CMO_parser import parse as cmo1
from .ABB1_parser import parse as abb1



from .SE_Parser import parce as se_parse
from .DKC_parcer import parce as dkc_parse
from .Phoenix_parser import parce as phoenix_parse
from .Rittal_parser import parce as rittal_parse
from .Wago_parser import parce as wago_parse
from .IEK_Parcer import parce as iek_parse
from .ITK_parcer import parce as itk_parse


def index(request):
    data = {
        'title': 'Парсер файлов с веб-страниц сайтов вендоров',
        'vendors': ['ABB',
                    "APC",
               "Bolid",
               "D-link", "DKC", 'Dahua',
               'Hikvision',
               "IEK", "ITK",
               "MikroTik",
               "Optimus",
               'Phoenix Contact',
               "Rittal",
               "Schneider Electric",
               "Ubiquiti", 'UNV',
               "Wago"],
        'version': 2.3
    }
    return render(request, 'main/index.html', data)

def abb(request):
    error = ''
    clear = ''
    value = 'Партномер:'
    description = 'Парсер собирает данные со страницы сайта new.abb.com по партномеру. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' и изображение позиции'
    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = ArticlesForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            try:
                abb1(form1.cleaned_data['partnumber'])
                clear = 'Готово. Проверьте каталог ABB_files'
            except:
                error = 'Ошибка. Проверьте ссылку'
        else:
            error = 'Ошибка. Неверный ввод'

    form = ArticlesForm()

    data = {
        'title': 'Парсер ABB',
        'form': form,
        'clear': clear,
        'value': value,
        'description': description,
        'error': error}

    return render(request, 'main/parser.html', data)

def apc(request):
    error = ''
    clear = ''
    value = 'Партномер:'
    description = 'Парсер собирает данные со страницы сайта apc.com по партномеру. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' и изображение позиции'
    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = ArticlesForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            try:
                apc1(form1.cleaned_data['partnumber'])
                clear = 'Готово. Проверьте каталог APC_files'
            except:
                error = 'Ошибка. Проверьте ссылку'
        else:
            error = 'Ошибка. Неверный ввод'

    form = ArticlesForm()

    data = {
        'title': 'Парсер APC',
        'form': form,
        'clear': clear,
        'value': value,
        'description': description,
        'error': error}

    return render(request, 'main/parser.html', data)




def bolid(request):
    error = ''
    clear = ''
    value = 'Ссылка на страницу продукта:'
    description = 'Парсер собирает данные со страницы сайта bolid.ru по ссылке. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' изображение позиции, а также файл с паспортом или руководством по эксплуатации'
    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = ArticlesForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            try:
                bolid1(form1.cleaned_data['partnumber'])
                clear = 'Готово. Проверьте каталог Bolid_files'
            except:
                error = 'Ошибка. Проверьте ссылку'
        else:
            error = 'Ошибка. Неверный ввод'

    form = ArticlesForm()

    data = {
        'title': 'Парсер Болид',
        'form': form,
        'clear': clear,
        'value': value,
        'description': description,
        'error': error}

    return render(request, 'main/parser.html', data)


def cmo(request):
    error = ''
    clear = ''
    value = 'Ссылка на страницу продукта:'
    description = 'Парсер собирает данные со страницы сайта cmo.ru по ссылке. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' изображение позиции, а также файл с паспортом'
    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = ArticlesForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            try:
                cmo1(form1.cleaned_data['partnumber'])
                clear = 'Готово. Проверьте каталог CMO_files'
            except:
                error = 'Ошибка. Проверьте ссылку'
        else:
            error = 'Ошибка. Неверный ввод'

    form = ArticlesForm()

    data = {
        'title': 'Парсер ЦМО',
        'form': form,
        'clear': clear,
        'value': value,
        'description': description,
        'error': error}

    return render(request, 'main/parser.html', data)


def dahua(request):
    error = ''
    clear = ''
    value = 'Ссылка на страницу продукта:'
    description = 'Парсер собирает данные по ссылке на сайт dahuasecurity.com. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' изображение позиции, а также даташит производителя. Вся текстовая информация переводится на русский в Google Translate'
    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = ArticlesForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            try:
                dahua1(form1.cleaned_data['partnumber'])
                clear = 'Готово. Проверьте каталог Dahua_files'
            except:
                error = 'Ошибка. Проверьте ссылку'
        else:
            error = 'Ошибка. Неверный ввод'

    form = ArticlesForm()

    data = {
        'title': 'Парсер Dahua',
        'form': form,
        'clear': clear,
        'value': value,
        'description': description,
        'error': error}

    return render(request, 'main/parser.html', data)


def dkc(request):
    error = ''
    clear = ''
    value = 'Партномер:'
    description = 'Парсер собирает данные по партномеру с сайта dkc.ru. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' изображение позиции, а также страница каталога производителя с описанием позиции'
    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = ArticlesForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            try:
                dkc1(form1.cleaned_data['partnumber'])
                clear = 'Готово. Проверьте каталог DKC_files'
            except:
                error = 'Ошибка. Проверьте артикул'
        else:
            error = 'Ошибка. Неверный ввод'

    form = ArticlesForm()

    data = {
        'title': 'Парсер DKC',
        'form': form,
        'clear': clear,
        'value': value,
        'description': description,
        'error': error}

    return render(request, 'main/parser.html', data)


def dlink(request):
    error = ''
    clear = ''
    value = 'Ссылка на страницу продукта:'
    description = 'Парсер собирает данные со страницы сайта dlink.ru(by) по ссылке. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' изображение позиции, а также файл описания производителя'
    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = ArticlesForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            try:
                dlink1(form1.cleaned_data['partnumber'])
                clear = 'Готово. Проверьте каталог Dlink_files'
            except:
                error = 'Ошибка. Проверьте ссылку'
        else:
            error = 'Ошибка. Неверный ввод'

    form = ArticlesForm()

    data = {
        'title': 'Парсер D-link',
        'form': form,
        'clear': clear,
        'value': value,
        'description': description,
        'error': error}

    return render(request, 'main/parser.html', data)


def hikvision(request):
    error = ''
    clear = ''
    value = 'Ссылка на страницу продукта:'
    description = 'Парсер собирает данные по ссылке на сайт hikvision.com. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' изображение позиции, а также даташит производителя. Вся текстовая информация переводится на русский в Google Translate'
    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = ArticlesForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            try:
                hikvision1(form1.cleaned_data['partnumber'])
                clear = 'Готово. Проверьте каталог Hikvision_files'
            except:
                error = 'Ошибка. Проверьте ссылку'
        else:
            error = 'Ошибка. Неверный ввод'

    form = ArticlesForm()

    data = {
        'title': 'Парсер Hikvision',
        'form': form,
        'clear': clear,
        'value': value,
        'description': description,
        'error': error}

    return render(request, 'main/parser.html', data)


def iek(request):
    error = ''
    clear = ''
    value = 'Партномер:'
    description = 'Парсер собирает данные данные по партномеру с сайта iek.ru. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' изображение позиции, а также файл руководства по эксплуатации и, если есть, краткое руководство по эксплуатации'
    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = ArticlesForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            try:
                iek1(form1.cleaned_data['partnumber'])
                clear = 'Готово. Проверьте каталог IEK_files'
            except:
                error = 'Ошибка. Проверьте артикул'
        else:
            error = 'Ошибка. Неверный ввод'

    form = ArticlesForm()

    data = {
        'title': 'Парсер IEK',
        'form': form,
        'clear': clear,
        'value': value,
        'description': description,
        'error': error}

    return render(request, 'main/parser.html', data)


def mikrotik(request):
    error = ''
    clear = ''
    value = 'Ссылка на страницу продукта:'
    description = 'Парсер собирает данные по ссылке на сайт mikrotik.com. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' изображение позиции, а также даташит производителя. Вся текстовая информация переводится на русский в Google Translate'
    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = ArticlesForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            try:
                mikrotik1(form1.cleaned_data['partnumber'])
                clear = 'Готово. Проверьте каталог Mikrotik_files'
            except:
                error = 'Ошибка. Проверьте ссылку'
        else:
            error = 'Ошибка. Неверный ввод'

    form = ArticlesForm()

    data = {
        'title': 'Парсер Mikrotik',
        'form': form,
        'clear': clear,
        'value': value,
        'description': description,
        'error': error}

    return render(request, 'main/parser.html', data)


def optimus(request):
    error = ''
    clear = ''
    value = 'Ссылка на страницу продукта:'
    description = 'Парсер собирает данные со страницы сайта optimus-cctv.ru по ссылке. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' изображение позиции, а также все файлы, которые прикреплены к позиции. В качестве имени файла используется партномер со страницы сайта'
    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = ArticlesForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            try:
                optimus1(form1.cleaned_data['partnumber'])
                clear = 'Готово. Проверьте каталог Optimus_files'
            except:
                error = 'Ошибка. Проверьте ссылку'
        else:
            error = 'Ошибка. Неверный ввод'

    form = ArticlesForm()

    data = {
        'title': 'Парсер Optimus',
        'form': form,
        'clear': clear,
        'value': value,
        'description': description,
        'error': error}

    return render(request, 'main/parser.html', data)


def phoenix(request):
    error = ''
    clear = ''
    value = 'Партномер:'
    description = 'Парсер собирает данные данные по партномеру с сайта phoenixcontact.com. Собирается и сохраняется информация с описанием выбранной позиции и' \
                  ' изображение позиции. Описание с первого раза может быть собрана не полная информация. Можно попробовать повторить'
    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = ArticlesForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            try:
                phoenix1(form1.cleaned_data['partnumber'])
                clear = 'Готово. Проверьте каталог Phoenix_files'
            except:
                error = 'Ошибка. Проверьте артикул'
        else:
            error = 'Ошибка. Неверный ввод'

    form = ArticlesForm()

    data = {
        'title': 'Парсер Phoenix Contact',
        'form': form,
        'clear': clear,
        'value': value,
        'description': description,
        'error': error}

    return render(request, 'main/parser.html', data)


def planet(request):
    error = ''
    clear = ''
    value = 'Ссылка:'
    description = 'Парсер собирает данные данные со страницы сайта www.planet.com.tw. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' изображение и все файлы позиции. Описание переводится в Google Translate. Перевод занимает много времени, порядка 2 минут на позицию.'
    if request.method == 'POST':
        form1 = ArticlesForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            # try:
                planet1(form1.cleaned_data['partnumber'])
                clear = 'Готово. Проверьте каталог Planet_files'
            # except:
            #     error = 'Ошибка. Проверьте ссылку'
        else:
            error = 'Ошибка. Неверный ввод'

    form = ArticlesForm()

    data = {
        'title': 'Парсер Planet',
        'form': form,
        'clear': clear,
        'value': value,
        'description': description,
        'error': error}

    return render(request, 'main/parser.html', data)


def rittal(request):
    error = ''
    clear = ''
    value = 'Партномер:'
    description = 'Парсер собирает данные данные по партномеру с сайта rittal.com/ru-ru. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' изображение позиции и файл с описанием производителя. '
    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = ArticlesForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            try:
                rittal1(form1.cleaned_data['partnumber'])
                clear = 'Готово. Проверьте каталог Rittal_files'
            except:
                error = 'Ошибка. Проверьте артикул'
        else:
            error = 'Ошибка. Неверный ввод'

    form = ArticlesForm()

    data = {
        'title': 'Парсер Rittal',
        'form': form,
        'clear': clear,
        'value': value,
        'description': description,
        'error': error}

    return render(request, 'main/parser.html', data)


def se(request):
    error = ''
    clear = ''
    value = 'Партномер:'
    description = 'Парсер собирает данные данные по партномеру с сайта se.com. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' изображение позиции и файл с описанием производителя. '
    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = ArticlesForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            try:
                se1(form1.cleaned_data['partnumber'])
                clear = 'Готово. Проверьте каталог SE_files'
            except:
                error = 'Ошибка. Проверьте артикул'
        else:
            error = 'Ошибка. Неверный ввод'

    form = ArticlesForm()

    data = {
        'title': 'Парсер Schneider Electric',
        'form': form,
        'clear': clear,
        'value': value,
        'description': description,
        'error': error}

    return render(request, 'main/parser.html', data)


def itk(request):
    error = ''
    clear = ''
    value = 'Партномер:'
    description = 'Парсер собирает данные данные по партномеру с сайта itk-group.ru. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' изображение позиции, а также файлы паспорта, руководства по эксплуатации и руководства по монтажу'
    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = ArticlesForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            try:
                itk1(form1.cleaned_data['partnumber'])
                clear = 'Готово. Проверьте каталог ITK_files'
            except:
                error = 'Ошибка. Проверьте артикул'
        else:
            error = 'Ошибка. Неверный ввод'

    form = ArticlesForm()

    data = {
        'title': 'Парсер ITK',
        'form': form,
        'clear': clear,
        'value': value,
        'description': description,
        'error': error}

    return render(request, 'main/parser.html', data)


def ubiquiti(request):
    error = ''
    clear = ''
    value = 'Ссылка на страницу продукта:'
    description = 'Парсер собирает данные по ссылке на сайт ubnt.su. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' изображение позиции, а также даташит производителя.'
    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = ArticlesForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            try:
                ubiquiti1(form1.cleaned_data['partnumber'])
                clear = 'Готово. Проверьте каталог Ubiquiti_files'
            except:
                error = 'Ошибка. Проверьте ссылку'
        else:
            error = 'Ошибка. Неверный ввод'

    form = ArticlesForm()

    data = {
        'title': 'Парсер Ubiquiti',
        'form': form,
        'clear': clear,
        'value': value,
        'description': description,
        'error': error}

    return render(request, 'main/parser.html', data)


def unv(request):
    error = ''
    clear = ''
    value = 'Ссылка на страницу продукта:'
    description = 'Парсер собирает данные по ссылке на сайт en.uniview.com. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' изображение позиции, а также даташит производителя. Вся текстовая информация переводится на русский в Google Translate'
    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = ArticlesForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            try:
                unv1(form1.cleaned_data['partnumber'])
                clear = 'Готово. Проверьте каталог UNV_files'
            except:
                error = 'Ошибка. Проверьте ссылку'
        else:
            error = 'Ошибка. Неверный ввод'

    form = ArticlesForm()

    data = {
        'title': 'Парсер Uniview',
        'form': form,
        'clear': clear,
        'value': value,
        'description': description,
        'error': error}

    return render(request, 'main/parser.html', data)

def wago(request):
    error = ''
    clear = ''
    value = 'Партномер:'
    description = 'Парсер собирает данные данные по партномеру с сайта wago.com. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' изображение позиции и файл с описанием производителя. '
    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = ArticlesForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            try:
                wago1(form1.cleaned_data['partnumber'])
                clear = 'Готово. Проверьте каталог Wago_files'
            except:
                error = 'Ошибка. Проверьте артикул'
        else:
            error = 'Ошибка. Неверный ввод'

    form = ArticlesForm()

    data = {
        'title': 'Парсер Wago',
        'form': form,
        'clear': clear,
        'value': value,
        'description': description,
        'error': error}

    return render(request, 'main/parser.html', data)










def se_mass(request):
    error = ''
    clear = ''
    value = 'Номера позиций прайса'
    price = 'main/price/se_price.xlsx'
    description = 'Парсер собирает данные данные с сайта se.com на основании прайса. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' изображение позиции и файл с описанием производителя. '

    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = NumbersForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            a = form1.cleaned_data['value_a']
            b = form1.cleaned_data['value_b']
            if int(a) > int(b):
                error = 'Ошибка. Неверный ввод'
            else:
                se_parse(a, b)
                clear = f'Готово: позиции прайса с {a} по {b} обработаны. Проверьте каталог SE_files'
        else:
            error = 'Ошибка. Неверный ввод'



    form = NumbersForm()

    data = {
        'title': 'Парсер Schneider Electric',
        'form': form,
        'clear': clear,
        'value': value,
        'price': price,
        'description': description,
        'error': error}

    return render(request, 'main/mass_parser.html', data)


def dkc_mass(request):
    error = ''
    clear = ''
    price = 'main/price/dkc_price.xlsx'
    value = 'Номера позиций прайса'
    description = 'Парсер собирает данные данные с сайта dkc.ru на основании прайса. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' изображение позиции и файл страницы каталога. '

    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = NumbersForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            a = form1.cleaned_data['value_a']
            b = form1.cleaned_data['value_b']
            if int(a) > int(b):
                error = 'Ошибка. Неверный ввод'
            else:
                dkc_parse(a, b)
                clear = f'Готово: позиции прайса с {a} по {b} обработаны. Проверьте каталог DKC_files'
        else:
            error = 'Ошибка. Неверный ввод'



    form = NumbersForm()

    data = {
        'title': 'Парсер DKC',
        'form': form,
        'clear': clear,
        'value': value,
        'price': price,
        'description': description,
        'error': error}

    return render(request, 'main/mass_parser.html', data)


def phoenix_mass(request):
    error = ''
    clear = ''
    price = 'main/price/phoenix_price.xlsx'
    value = 'Номера позиций прайса'
    description = 'Парсер собирает данные данные с сайта phoenixcontact.com на основании прайса. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' изображение позиции и файл страницы каталога. Сайт открывается через эмуляцию открытия в браузере и двемя вкладками.' \
                  ' С первого раза система может собрать не все данные из-за блокирования сайтом повторного запроса'

    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = NumbersForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            a = form1.cleaned_data['value_a']
            b = form1.cleaned_data['value_b']
            if int(a) > int(b):
                error = 'Ошибка. Неверный ввод'
            else:
                phoenix_parse(a, b)
                clear = f'Готово: позиции прайса с {a} по {b} обработаны. Проверьте каталог Phoenix_files'
        else:
            error = 'Ошибка. Неверный ввод'



    form = NumbersForm()

    data = {
        'title': 'Парсер Phoenix Contact',
        'form': form,
        'clear': clear,
        'value': value,
        'price': price,
        'description': description,
        'error': error}

    return render(request, 'main/mass_parser.html', data)



def rittal_mass(request):
    error = ''
    clear = ''
    price = 'main/price/rittal_price.xlsx'
    value = 'Номера позиций прайса'
    description = 'Парсер собирает данные данные по партномеру с сайта rittal.com/ru-ru. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' изображение позиции и файл с описанием производителя. '

    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = NumbersForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            a = form1.cleaned_data['value_a']
            b = form1.cleaned_data['value_b']
            if int(a) > int(b):
                error = 'Ошибка. Неверный ввод'
            else:
                rittal_parse(a, b)
                clear = f'Готово: позиции прайса с {a} по {b} обработаны. Проверьте каталог Rittal_files'
        else:
            error = 'Ошибка. Неверный ввод'

    form = NumbersForm()

    data = {
        'title': 'Парсер Rittal',
        'form': form,
        'clear': clear,
        'value': value,
        'price': price,
        'description': description,
        'error': error}

    return render(request, 'main/mass_parser.html', data)


def wago_mass(request):
    error = ''
    clear = ''
    price = 'main/price/wago_price.xlsx'
    value = 'Номера позиций прайса'
    description = 'Парсер собирает данные данные по партномеру с сайта wago.com. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' изображение позиции и файл с описанием производителя. '

    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = NumbersForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            a = form1.cleaned_data['value_a']
            b = form1.cleaned_data['value_b']
            if int(a) > int(b):
                error = 'Ошибка. Неверный ввод'
            else:
                wago_parse(a, b)
                clear = f'Готово: позиции прайса с {a} по {b} обработаны. Проверьте каталог Wago_files'
        else:
            error = 'Ошибка. Неверный ввод'

    form = NumbersForm()

    data = {
        'title': 'Парсер Wago',
        'form': form,
        'clear': clear,
        'value': value,
        'price': price,
        'description': description,
        'error': error}

    return render(request, 'main/mass_parser.html', data)



def iek_mass(request):
    error = ''
    clear = ''
    price = 'main/price/iek_price.xlsx'
    value = 'Номера позиций прайса'
    description = 'Парсер собирает данные данные по партномеру с сайта iek.ru. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' изображение позиции, а также файл руководства по эксплуатации и, если есть, краткое руководство по эксплуатации'

    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = NumbersForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            a = form1.cleaned_data['value_a']
            b = form1.cleaned_data['value_b']
            if int(a) > int(b):
                error = 'Ошибка. Неверный ввод'
            else:
                iek_parse(a, b)
                clear = f'Готово: позиции прайса с {a} по {b} обработаны. Проверьте каталог IEK_files'
        else:
            error = 'Ошибка. Неверный ввод'

    form = NumbersForm()

    data = {
        'title': 'Парсер IEK',
        'form': form,
        'clear': clear,
        'value': value,
        'price': price,
        'description': description,
        'error': error}

    return render(request, 'main/mass_parser.html', data)


def itk_mass(request):
    error = ''
    clear = ''
    price = 'main/price/itk_price.xlsx'
    value = 'Номера позиций прайса'
    description = 'Парсер собирает данные данные по партномеру с сайта itk-group.ru. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' изображение позиции, а также файлы паспорта, руководства по эксплуатации и руководства по монтажу'

    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = NumbersForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            a = form1.cleaned_data['value_a']
            b = form1.cleaned_data['value_b']
            if int(a) > int(b):
                error = 'Ошибка. Неверный ввод'
            else:
                itk_parse(a, b)
                clear = f'Готово: позиции прайса с {a} по {b} обработаны. Проверьте каталог ITK_files'
        else:
            error = 'Ошибка. Неверный ввод'

    form = NumbersForm()

    data = {
        'title': 'Парсер ITK',
        'form': form,
        'clear': clear,
        'value': value,
        'price': price,
        'description': description,
        'error': error}

    return render(request, 'main/mass_parser.html', data)
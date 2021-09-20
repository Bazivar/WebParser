from django.shortcuts import render
from .forms import ArticlesForm
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

def index(request):
    data = {
        'title': 'Парсер файлов с веб-страниц сайтов вендоров',
        'vendors': ["Bolid",
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
        'version': 2.0
    }
    return render(request, 'main/index.html', data)

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


def dahua(request):
    error = ''
    clear = ''
    value = 'Ссылка на страницу продукта:'

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
        # 'description': description,
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


def optimus(request):
    error = ''
    clear = ''
    value = 'Ссылка на страницу продукта:'
    description = 'Парсер собирает данные со страницы сайта optimus-cctv.ru по ссылке. Собирается и сохраняется информация с описанием выбранной позиции,' \
                  ' изображение позиции, а также все файлы, которые прикреплены к позиции. В качестве имени файла используется партномер со страницы сайта'
    if request.method == 'POST':  # если метод передачи данных на страницу соответствует тому, что мы задали на странице create.html
        form1 = ArticlesForm(request.POST)
        if form1.is_valid():  # проверка на корректность введённых данных
            # try:
                optimus1(form1.cleaned_data['partnumber'])
                clear = 'Готово. Проверьте каталог Optimus_files'
            # except:
            #     error = 'Ошибка. Проверьте ссылку'
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
            # try:
                phoenix1(form1.cleaned_data['partnumber'])
                clear = 'Готово. Проверьте каталог Phoenix_files'
            # except:
            #     error = 'Ошибка. Проверьте артикул'
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
from django.shortcuts import render
from .forms import ArticlesForm
from .SE1_parser import parce as se1

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

def se(request):
    error = ''
    clear = ''
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
        'title': 'Сбор данных для Schneider Electric',
        'form': form,
        'clear':clear,
        'error': error}
    return render(request, 'main/se.html', data)
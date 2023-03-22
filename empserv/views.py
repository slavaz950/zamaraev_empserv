from django.http import HttpResponse  # Передача текста или небольшого html-кода
from django.shortcuts import render   # Передача html-файлов



"""  Comment  """



def testone (request):
    return HttpResponse('This is 1978 page')  
       
# Параметр request означает что каждый раз когда кто-то ищет какую-то веб-страницу он отправляет запрос (request)
# То есть запрос url который он хочет. Также этот (request) содержит куки, какой используется браузер и т.д.

def testtwo (request):
    return HttpResponse('This is 2000')  

# Также здесь в качестве параметра мы можем передавать какой-то html-код 
# Но если объём кода большой то не нужно делать этого в HttpResponse

# Для использования html-кода мы будем использовать templates (шаблоны)
# Создадим в корневой папке новую папку templates.
# В этой папке будем хранить html-файлы.
# Нам нужно пользователя каждый раз перенаправлять на нужную ему html-страницу
# Прежде всего нужно объяснить Django где искать эти шаблоны 

# В файле settings.py находим раздел TEMPLATES там находим DIRS лист
# Здесь мы можем указывать те места в которых Django должен искать шаблоны
# Вносим туда созданную нами папку templates. Пока у на здесь один элемент,
# но их может быть достаточно много.
#

def home_test (request):
    return render(request, 'home_test.html')

def main_test (request):
    return render(request, 'main_test.html')

def reverse_test(request):
    user_text = request.GET['usertexttest']  #  В [] указываем ключ параметра который мы ищем.
    # Ключ этот можно найти в  атрибуте  name  формы находящейся в html файле.
    # В нашем случае в файле reverse_test.html (атрибут формы name="usertexttest")
    
    # Для проверки, чтобы видеть получаем мы эту информацию или нет можно
    # написать следующую строку
   # test_get_text = request.GET['usertexttest']
   # print(test_get_text)
    # Создаём переменную test_get_text и присвоим ей значение request.GET['usertexttest']
    # print выводит значение test_get_text на консоль
    #
    words = user_text.split() # Получаем список слов находящихся в переменной
    number_of_words = len(words) # Считаем количество слов
    reverse_text = user_text[::-1] # Разворачиваем строку наоборот
    return render(request,'reverse_test.html', {'usertext':user_text,'reversedtext':reverse_text,})
# В фигурных скобках {} расположены две пары ключ-значение  

# По первой паре 'usertext' мы будем получать информацию из переменной user_text. То есть каждый раз когда
# мы будем ссылаться на этот ключ в нашем html файле мы будем получать этот текст. На html странице
# нужно указать значение этого ключа в фигурных скобках {{usertext}}

# Вторая пара 'reversedtext' работает аналогично, только значения другие
#
#
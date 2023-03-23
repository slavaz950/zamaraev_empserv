"""empserv URL Конфигурация

Список `urlpatterns` направляет URL-адреса в представления. Для получения дополнительной информации см.:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Примеры:
Представления функций
     1. Добавьте импорт:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add aДобавьте URL-адрес в urlpatterns:  path('', Home.as_view(), name='home')
В том числе другой URLconf
    1. Импортируйте функцию include(): from django.urls import include, path
    2. Добавить URL-адрес в шаблоны URL-адресов:  path('blog/', include('blog.urls'))



"""

"""  Comment  """

from django.contrib import admin
from django.urls import path
from.import views # То есть из той же папки где лежит файл urls.py импортируем views.py
from django.conf import settings # Импортируем settings.py
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls), 

# Здесь мы можем установить наши собственные пути 

    path('testone/',views.testone),
    # Функция  path задаёт сопоставление определённого маршрута с соответствующей функцией 
    # обработки
    # Первым параметром определяем маршрут
    # Вторым параметром указываем Файл views и дальше указуваем соответствующую функцию из views.py это about
    # Также дополнительно третьим параметром можно указать имя маршрута. Например name = 'About page'
    # Вместе с третьим параметром запись будет path('about/', views.about, name = 'About page'),

# Нужно связать about с каким-то python файлом, которым мы можем устанавливать какой-то текст 
# Нужно создать в этой же папке файл views.py (если его нет). Теперь здесь в urls.py мы должны  
# импортировать views.py.


# path() ограничена по своему действию. Запрошенный путь должен в точности соответствовать 
# на странице указанному в маршруте адресу url. 

# re_path() позволяет задавать адреса с помощью регулярных выражений
#
#

    path('testtwo/', views.testtwo),
    path('home_test/', views.home_test),
    path('', views.main_test), 
    path('reverse_test/', views.reverse_test),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Указываем где искать медиа-файлы
# Эта строка используется для управления любыми медиа-файлами (видео, картинки, аудио) на нашем сайте
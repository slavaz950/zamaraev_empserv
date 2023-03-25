from django.shortcuts import render
from .models import Events  # Экспорт модели events

def home(request):
   events = Events.objects # Получаем все объекты events из БД и сохраняем их в переменной
   return render (request, 'events/home.html', {'events': events})
    # Передаём информацию при помощи словаря (третьим параметром). Указываем ключ 'events'
    # и связываем его с переменной events
    
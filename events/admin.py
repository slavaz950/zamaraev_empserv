from django.contrib import admin
from.models import Events  # Импортируем наш класс Events

# Зарегистрируйте свои модели здесь.

admin.site.register(Events) # Передаём нашу модель 


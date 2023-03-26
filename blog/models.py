from django.db import models

# Create your models here.

class Post (models.Model):
    title = models.CharField(max_length=300) # Заголовок. Символьный тип данных
    date = models.DateTimeField()   # Дата и время
    text = models.TextField()  # Текстовое поле. Текстовый тип данных
    image = models.ImageField(upload_to='event_images/')  # Изображение

    def get_summary(self): # Ограничивает вывод символов из свойства text до 70
        return self.text[:70] # Выводит свойство text текущей модели 


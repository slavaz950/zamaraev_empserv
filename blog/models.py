from django.db import models

# Create your models here.

class Post (models.Model):
    title = models.CharField(max_length=300) # Заголовок. Символьный тип данных
    date = models.DateTimeField()   # Дата и время
    text = models.TextField()  # Текстовое поле. Текстовый тип данных
    image = models.ImageField(upload_to='event_images/')  # Изображение

    def get_summary(self): # Ограничивает вывод символов из свойства text до 70
        return self.text[:70] # Выводит свойство text текущей модели 

    def __str__(self):
        return self.title
# Функция __str__ используется каждый раз когда Django хочет показать объекты в Админке
# то есть здесь мы сможем вернуть всё что угодно. В данном случае мы возвращаем заголовок 
# этого поста (title). Функция должна быть написана именно здесь в класс (то есть внутри
# самой модели)


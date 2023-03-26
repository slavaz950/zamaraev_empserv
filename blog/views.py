from django.shortcuts import render, get_object_or_404 # Импорт функции get_object_or_404
# Суть функции get_object_or_404 в том что она либо получает объекты из БД, либо 
# если не находит объект по этому ID в БД то она возвращает страницу 404 
# пользователь перенаправляется на страницу 404 (нет такого url который вы ищете)
from .models import Post

# Create your views here.
def showblog(request):
    posts = Post.objects
    return render(request, 'blog/blog.html', {'posts': posts})

def specific_post(request, post_id):  # По post_id получаем конкретный пост из БД    <int:post_id>
    post = get_object_or_404(Post, pk=post_id) 
     # Передаём модель которую мы ищем (Post), 
   # указываем параметр pk то есть (Primary Key) - основной ключ. Ключ этого объекта в БД 
      
    return render(request, 'blog/specific_post.html', {'post': post})   
      
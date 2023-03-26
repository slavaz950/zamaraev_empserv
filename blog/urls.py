from django.urls import path
from . import views

urlpatterns = [

    path('', views.showblog, name='showblog'),
    path('<int:post_id>/', views.specific_post, name='specific_post'),
    # Запись <int:post_id>/ означает что Django будет сохранять целое число (int)
    # которое будет получать в urlе в переменной post_id
    # Далее ссылаемся на функцию specific_post находящуюся в views
    #
]
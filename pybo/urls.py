from django import views
from django.urls import path
from .views import index, detail, answer_create, question_create
# from . import views --> views.detail , views.index

app_name = 'pybo'

urlpatterns = [
    path('', index, name='index'),
    path('<int:question_id>/', detail, name='detail'),
    path('answer/create/<int:question_id>/', answer_create, name='answer_create'),
    path('question/create/', question_create, name='question_create'),
    # config/urls.py에서 'pybo/' + '' --> 'pybo/'
]

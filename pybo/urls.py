from django.urls import path
# from .views import index, detail, answer_create
from . import views

app_name = 'pybo'
urlpatterns = [
    path('', views.index, name='index'),    # config/urls.py에서 'pybo/' + '' --> 'pybo/'
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, 
         name='answer_create'),

]
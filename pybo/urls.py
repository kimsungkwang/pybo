from django.urls import path
# from .views import index, detail, answer_create
from . import views


# Function Based View: FBV
app_name = 'pybo'
urlpatterns = [
    path('', views.index, name='index'),    # config/urls.py에서 'pybo/' + '' --> 'pybo/'
    path('<int:question_id>/', views.detail, name='detail'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modefy'),
    path('answer/create/<int:question_id>/', views.answer_create, 
         name='answer_create'),
    
]
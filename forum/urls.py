from django.urls import path
from forum.views import *

app_name = 'forum'

urlpatterns = [
    path('', question_list, name='question_list'),
    path('question/<int:pk>/', question_detail, name = 'question_detail'),
    path('question/add/', add_question, name = 'add_question'),
    path('question/<int:pk>/answer/', add_answer, name = 'add_answer')
]
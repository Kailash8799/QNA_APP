from django.urls import path
from . import views

urlpatterns = [
    path("question/",views.question,name="que"),
    path("questions_ans/",views.answer,name="ans"),
]

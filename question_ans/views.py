from django.shortcuts import render,redirect
from .models import Question
from .forms import QuestionForm
# Create your views here.

def question(request):
    params = {'que':""}
    if(request.method == "GET"):
        total_que = Question.objects.all()
        params = {'que':total_que}
    return render(request,"qna/all_que.html",params)   
 
def askquestion(request):
    if(request.method == "POST"):
        form = QuestionForm(request.POST)
        params = {'form':form}
    else:
        form = QuestionForm()
        params = {'form':form}
    return render(request,"qna/all_que.html",params)    
def answer(request):
    params = {'form':''}
    if(request.method == "POST"):
        form = QuestionForm(request.POST)
        params = {'form':form}
    else:
        form = QuestionForm()
        params = {'form':form}
    return render(request,"qna/que_ans.html",params)    
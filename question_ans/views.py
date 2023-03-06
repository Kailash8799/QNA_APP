import json
from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from .models import Question,Answer,Contact
from auth_credentials.models import Users
from .forms import QuestionForm,AnswerForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def question(request):
    params = {'que':""}
    if(request.method == "GET"):
        total_que = Question.objects.all().order_by('-date_created')
        params = {'que':total_que}
    return render(request,"qna/all_que.html",params)   

@login_required
def askquestion(request):
    if request.user.is_authenticated == False:
        messages.warning(request,"Login required for ask question")
        return redirect('/')
    if(request.method == "POST"):
        que = Question(user=request.user,title=request.POST.get('title'),tags=request.POST.get('tags'),content=request.POST.get('content'))
        que.save()
        form = QuestionForm()
        messages.success(request,"Your question will be registered")
        params = {'form':form}
    else:
        form = QuestionForm()
        params = {'form':form}
    return render(request,"qna/ask.html",params)  
  
def que_desc(request,id):
    que = Question.objects.filter(que_id=id)
    if(len(que) == 0):
         return redirect("/question_ans/question/")
    ques = que
    for q in que:
        que = q
    vis = que.total_views + 1
    ques.update(total_views=vis)
    tags = que.tags
    tags = tags.split(" ")
    answers = Answer.objects.filter(que_ans=que.que_id).order_by('-date_created')
    form = AnswerForm()
    params = {'form':form,'ques':que,'answer':answers,'tags':tags}
    return render(request,"qna/que_ans.html",params)    


def answer(request):
    params = {'form':''}
    if(request.method == "POST"):
        form = QuestionForm(request.POST)
        params = {'form':form}
    else:
        form = QuestionForm()
        params = {'form':form}
    return render(request,"qna/que_ans.html",params) 

@login_required   
def contact(request):
    if(request.method == "POST"):
        message = request.POST.get("message","")
        cont = Contact(user=request.user,desc=message)
        cont.save()
        messages.success(request,"Successfully Sent!!")
        return redirect("/question_ans/contact/")
    return render(request,"qna/contact.html")    

@login_required
def delete_ans(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        id = data['id']
        if(id != None):
            Answer.objects.filter(ans_id = id).delete()
            return JsonResponse({"msg":"success"})
        else:
            return JsonResponse({"msg":"error"})

@login_required
def give_ans(request):
    if(request.method == 'POST'):
        qid = request.POST.get('id','')
        ans = request.POST.get('answer','')
        que_a = Question.objects.filter(que_id=qid).first()
        ansque = Answer(user=request.user,que_ans=que_a,answer=ans)
        ansque.save()
        return redirect(f"/question_ans/description_que/id={qid}/")

@login_required
def likes_ques(reqest):
    pass

@login_required
def delete_que(request):
    pass

def about(request):
    return render(request,"qna/about.html")
def teams(request):
    return render(request,"qna/teams.html")
def product(request):
    return render(request,"qna/product.html")

def search(request):
    params = {'que':""}
    query = request.GET.get('query','')
    total_que = Question.objects.none()
    if(request.method == "GET" and len(query) < 50 and (query)):
        titlecontain = Question.objects.filter(title__icontains=query)
        contentcontain = Question.objects.filter(content__icontains=query)
        total_que = titlecontain.union(contentcontain).order_by('-date_created')
    params = {'que':total_que,'query':query}
    return render(request,"qna/search.html",params)   

def page404(request):
    return HttpResponse("404")
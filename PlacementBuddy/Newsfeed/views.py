from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Post,Comment,FavouritePost,Question
from .question_splitter import *
from Home.models import User
from .models import Question
# Create your views here.
import datetime

#Routing for Newsfeed
class Newsfeed(View):

    @csrf_exempt
    def get(self,request):
        logined_user = request.session.get("logined_user")
        logined_user_obj = User.objects.get(name=logined_user)
        context={"user_name":logined_user}
        if 'comment' in request.GET:
            print("Inside post")

            post_obj = Post.objects.get(id = request.GET.get('post_id'))
            print("Creating comment object")
            comment = Comment(user = logined_user_obj,post=post_obj,comment = request.GET.get('comment'))
            comment.save()
            print("Saved comment object")
            return JsonResponse({'profile_pic_url':logined_user_obj.profile_pic.url,'comment_user':logined_user})
        elif 'star' in request.GET:
            logined_user = request.session.get("logined_user")
            logined_user_obj = User.objects.get(name=logined_user)
            post_obj = Post.objects.get(id = request.GET.get('post_id'))
            try:
                fav_post_obj = FavouritePost.objects.get(user=logined_user_obj,post=post_obj)
            except:
                fav_post_obj = None
            print("fav_post_obj over",fav_post_obj)
            if fav_post_obj == None:
                fav_post_obj = FavouritePost(user=logined_user_obj,post=post_obj)
                fav_post_obj.save()
            else:
                fav_post_obj.delete()
            return JsonResponse({})

        else:    
            logined_user = request.session.get("logined_user")
            if not logined_user:
                print("Not logined")
                return redirect('signin')
            posts = reversed(Post.objects.all())
            context["posts"]=posts

            css_class_active = {'all_posts':'option-active'}

            context["css_class_active"]=css_class_active  
            return render(request, 'newsfeed.html',context=context)


def fav_posts(request):
    logined_user = request.session.get("logined_user")
    logined_user_obj = User.objects.get(name=logined_user)
    fav_posts = FavouritePost.objects.filter(user = logined_user_obj)
    fav_posts = [fav_post.post for fav_post in fav_posts]    
    context={"user_name":logined_user,'fav_posts':fav_posts}
    print(fav_posts)
    css_class_active = {'fav_posts':'option-active'}

    context["css_class_active"]=css_class_active  
    return render(request, 'starred_posts.html',context=context)

def all_questions(request):
    context={}
    q = Question.objects.all()
    if request.method=="GET":
        context['questions'] = q
        context['subject'] = "Questions"

        print(request.GET)
    css_class_active = {'questions':'option-active'}
    context["css_class_active"]=css_class_active 
    return render(request, 'all_questions.html',context=context)
def algorithm_questions(request):
    context={}
    q = Question.objects.all()
    q = q.filter(subject="Data Strutures and Algorithms")
    if request.method=="GET":
        context['questions'] = q
        context['subject'] = "DS and Algorithms"
        
        print(request.GET)
    css_class_active = {'questions':'option-active'}
    context["css_class_active"]=css_class_active 
 
    return render(request, 'all_questions.html',context=context)
def programming_questions(request):
    context={}
    q = Question.objects.all()
    q = q.filter(subject="Programming")

    if request.method=="GET":
        context['questions'] = q
        context['subject'] = "Programming"
        print(request.GET)
    css_class_active = {'questions':'option-active'}
    context["css_class_active"]=css_class_active 
 
    return render(request, 'all_questions.html',context=context)
def dbms_questions(request):
    context={}

    q = Question.objects.all()
    q = q.filter(subject="DBMS")

    if request.method=="GET":
        context['questions'] = q
        context['subject'] = "DBMS"
        print(request.GET)
    css_class_active = {'questions':'option-active'}
    context["css_class_active"]=css_class_active 
 
    return render(request, 'all_questions.html',context=context)

def cn_questions(request):
    context={}

    q = Question.objects.all()
    q = q.filter(subject="Computer Networks")

    if request.method=="GET":
        context['questions'] = q
        context['subject'] = "Computer Networks"
        print(request.GET)
    css_class_active = {'questions':'option-active'}
    context["css_class_active"]=css_class_active 
 
    return render(request, 'all_questions.html',context=context)

def sw_questions(request):
    context={}

    q = Question.objects.all()
    q = q.filter(subject="Software Engineering")

    if request.method=="GET":
        context['questions'] = q
        context['subject'] = "Software Engineering"
        print(request.GET)
    css_class_active = {'questions':'option-active'}
    context["css_class_active"]=css_class_active 
 
    return render(request, 'all_questions.html',context=context)



class PostReview(View):    
    def get(self,request):
        logined_user = request.session.get("logined_user")
        if not logined_user:
            print("Not logined")
            return redirect('signin')
        context={"user_name":logined_user}
        css_class_active = {'post_review':'option-active'}
        
        context["css_class_active"]=css_class_active        
        return render(request, 'post_review.html',context=context)    
    def post(self,request):
        logined_user = request.session.get("logined_user")
        context={}

        my_date = datetime.datetime.now()
        date_now = str(my_date)[:-10]
        year = date_now[:4]
        date = date_now[8:10]
        month = my_date.strftime("%B")
        time = f'{month} {date} {year} at {date_now[11:]}'
        logined_user_obj = User.objects.get(name=logined_user)
        post = Post(
                      user=logined_user_obj,
                      date = date_now,
                      time= time,
                      job_title=request.POST.get('job_title'),
                      company = request.POST.get('company'),
                      difficulty = request.POST.get('difficulty'),
                      experience = request.POST.get('experience'),
                      questions =[] 
                      )
        questions =[]
        i = 1
        while request.POST.get('question-'+str(i)):
            ques = request.POST.get('question-'+str(i))
            if ques[-1]=="?":
                ques=ques[:-1]
            questions.append(ques)
            i+=1
        post.questions = questions
        post.save()

        final_res = get_catogarized_questions(questions)
        for topic in final_res:
            for question in final_res[topic]:
                q = Question(post=post,question=question,subject=topic)
                q.save()
        print(request.POST)


        return redirect('newsfeed')    
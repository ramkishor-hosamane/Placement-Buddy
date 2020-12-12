from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Post,Comment,FavouritePost
from Home.models import User
# Create your views here.


#Routing for Newsfeed
class Newsfeed(View):

    @csrf_exempt
    def get(self,request):
        if 'comment' in request.GET:
            print("Inside post")
            logined_user = request.session.get("logined_user")
            logined_user_obj = User.objects.get(name=logined_user)
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
            context={"user_name":logined_user}
            posts = Post.objects.all()
            print(posts[0].favouritepost_set.all())
            context={"user_name":logined_user,"posts":posts}  
            return render(request, 'newsfeed.html',context=context)


def fav_posts(request):
    logined_user = request.session.get("logined_user")
    logined_user_obj = User.objects.get(name=logined_user)
    fav_posts = FavouritePost.objects.filter(user = logined_user_obj)
    fav_posts = [fav_post.post for fav_post in fav_posts]    
    context={"user_name":logined_user,'fav_posts':fav_posts}
    print(fav_posts)
    return render(request, 'starred_posts.html',context=context)

class PostReview(View):    
    def get(self,request):
        logined_user = request.session.get("logined_user")
        if not logined_user:
            print("Not logined")
            return redirect('signin')
      
        return render(request, 'post_review.html')    
    def post(self,request):
        logined_user = request.session.get("logined_user")
        context={}
        logined_user_obj = User.objects.get(name=logined_user)
        post = Post(
                      user=logined_user_obj,
                      date = str(datetime.datetime.now())[:-10],
                      job_title=request.POST.get('job_title'),
                      company = request.POST.get('company'),
                      difficulty = request.POST.get('difficulty'),
                      experience = request.POST.get('experience'),
                      questions =[] 
                      )
        i = 1
        while request.POST.get('question-'+str(i)):
            post.questions.append(request.POST.get('question-'+str(i)))
            i+=1
        print(request.POST)


        post.save()
        return redirect('newsfeed')    
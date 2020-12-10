from django.shortcuts import render,redirect
from django.views import View
# Create your views here.


#Routing for Newsfeed
class Newsfeed(View):    
    def get(self,request):
        logined_user = request.session.get("logined_user")
        if not logined_user:
            print("Not logined")
            return redirect('signin')
        context={"user_name":logined_user}
        return render(request, 'newsfeed.html',context=context)
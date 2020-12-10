from django.shortcuts import render,redirect,reverse
from django.views import View
from .models import User
# Create your views here.


#Routing for Home
def home(request):

    print("Logined user is ",request.session.get('logined_user'))
    return render(request, 'home.html')


#Routing for Signup
class Signup(View):
        
    def get(self,request):
        return render(request,'signup.html')

    def post(self,request):
        
        #Getting data from signup form
        user_name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        profile_pic = request.FILES.get('profile_pic')
        phone_number = request.POST.get('phonenumber')


        #All users in the database
        all_users = User.objects.all()
        
        #Querying if user is there in database or not
        user_query_set = all_users.filter(email=email)
        
        #If entered user name is not there create it and goto login page
        if len(user_query_set) == 0:
            #Adding User account data to Django SQL database
            user = User(name = user_name,password = password,email =email,phone_number = phone_number,profile_pic = profile_pic)
            user.save()
            return redirect('signin')

        print("Signup Failed")
        error_msg= "Email already exists"
        context = {'error_msg':error_msg}
        return render(request,'signup.html',context=context)      





#Routing for Signin
class Signin(View):
    login_info = {"is_logined":False,"user_name":""} 
    def get(self,request):
        if request.path == "/logout":
            request.session['logined_user'] = None
            print("Loging out")
        return render(request, 'signin.html')
    
    def post(self,request):
        all_users = User.objects.all()
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        #Querying if user is there in database or not
        user_query_set = all_users.filter(email=email,password=password)
        if len(user_query_set) > 0 :
                 print("Logined successfully")
                 request.session['logined_user'] = user_query_set[0].name
                 #return redirect('newsfeed/'+user.name)                 
                 return redirect('signin')

        print("Login Failed")
        error_msg= "Wrong email or password"
        context = {'error_msg':error_msg}
        return render(request,'signin.html',context=context)
                

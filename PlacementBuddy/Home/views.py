from django.shortcuts import render,redirect,reverse
from django.views import View
from .models import User
# Create your views here.


#Routing for Home
def home(request):
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
        
        print("Added User")
        print("Other things ",user_name,password,email,phone_number)
        
        ''' 
        
            Over to you Akanksha 
            All the best !!!!!!!
            
            update :=> Failed
        
        '''
        #Adding User account data to Django SQL database
        user = User(name = user_name,password = password,email =email,phone_number = phone_number,profile_pic = profile_pic)
        user.save()

        return render(request,'signup.html')




#Routing for Signin
class Signin(View):
    login_info = {"is_logined":False,"user_name":""} 
    def get(self,request):
        if request.path == "/logout":
            login_info = {"is_logined":False,"user_name":""}
            print("Loging out")
        return render(request, 'signin.html')
    
    def post(self,request):
        all_users = User.objects.all()
        password = request.POST.get('password')
        email = request.POST.get('email')
        print('login')
        for user in all_users:
            if user.email == email and user.password == password:
                 Signin.login_info['is_logined'] = True
                 Signin.login_info['user_name'] = user.name
                
                 return redirect('newsfeed/'+user.name)                 

        error_msg= "Wrong email or password"
        context = {'error_msg':error_msg}
        return render(request,'signin.html',context=context)
                

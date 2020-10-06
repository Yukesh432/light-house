from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
<<<<<<< HEAD
from .models import UserProfile
=======
>>>>>>> dd68b189e98b072c2f8fac59112139352088294d

# def register(request):
#     return render(request, 'accounts/register.html')
def register(request):
    if request.method == 'POST':
        #get form values
        first_name= request.POST['fname']
        last_name= request.POST['lname']
        username= request.POST['username'] 
        email= request.POST['email']
        password= request.POST['password'] 
        password2= request.POST['password2'] 
        phone = request.POST['phone']
        # print("PPPPOOOPPPP")
        # userprofile= UserProfile()
        # userprofile.user = User.username
        
        # print(userprofile.user)        

        if password == password2:
            #check username
            if User.objects.filter(username= username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email= email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    user= User.objects.create_user(username= username, password= password, email= email, first_name= first_name, last_name= last_name)
                    # auth.login(request, user)
                    # messages.success(request, 'you are now logged in')
                    user.save()
                    
                    subject = 'Thank you for pre-order from Sampannalighthouse'
                    message = "Welcome to Sampanna Light House. We are vey glad that you logged in to our website./n So, enjoy your day!"
                    from_email = settings.EMAIL_HOST_USER
                    to_list = [user.email, settings.EMAIL_HOST_USER]
                    send_mail(subject, message, from_email, to_list, fail_silently= True)


                    messages.success(request, 'you are now registered in')
                    return redirect('login')
        else:
            messages.error(request, 'Password donot match')
            return redirect('register')

        #create UserProfile Form

    
        # userprofile.phone = phone
        # userprofile.email = email
        # userprofile.gender = request.POST.get('gender')
        # userprofile.address = "-"
        # userprofile.save()
            
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # print(email)
        print(password)

        user= auth.authenticate(username= username, password= password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')

def logout(request):

    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('login') 




def recovery(request):
    return render(request, 'accounts/login.html')

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
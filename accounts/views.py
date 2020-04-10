from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.
def register(request):
    print('========register=============')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        if User.objects.filter(username=username):
            messages.info(request, "Username Exist!")
            return redirect('register')
        elif User.objects.filter(email=email):
            messages.info(request, "Email Exist!")
            return redirect('register')
        elif confirm_password != password:
            messages.info(request, "Password not matching ...., Please check and try agian!")
            return redirect('register')
        else:
            print('========create user=============')
            # create user
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            # save user to db
            user.save()
            print('========create user done=============')
            return redirect('login')
    else:
        return render(request, 'register.html')

def login(request):
    print('========login=============')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print('========login done=============')
            return redirect('/')
        else:
            messages.info(request, "User not exist, pls check!")
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
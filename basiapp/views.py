from django.shortcuts import render, redirect
from basiapp.forms import Userform, Portfolio
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,logout, login
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def userform(request):
    form = Userform()
    form1 = Portfolio()
    registered = False

    if request.method == "POST":
        form = Userform(request.POST)
        form1 = Portfolio(request.POST)

        if form.is_valid() and form1.is_valid():
            user = form.save(commit=True)
            user.set_password(user.password)# password is a function which created in forms and not in model. Since, it is no were
            #saved in database. So, to save the password in DB, we are passing the value again to object.set_password()and it also hash the password
            user.save()

            #since portfolio is a second form, saving it with commit=true may overwrite the previous existing data.
            #To prevent that, commit is made as False
            portfolio_user = form1.save(commit=False)
            portfolio_user.user = user
            # establishing one to one relationship between two forms

            if 'profile_pic' in request.FILES:
                portfolio_user.profile_pic = request.FILES['profile_pic']

            portfolio_user.save()
            registered = True

        else:
            print(form.errors,form1.errors)

    else:
        form = Userform()
        form1 = Portfolio()

    return render(request,'basiapp/forms.html',{'form':form,'form1':form1,'registered':registered})


def user_login(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                print("logged in")
                return HttpResponseRedirect(reverse('index'))
                #return redirect(request,"basiapp/index.html",{'user':user})

            else:
                print("error")
                return render(request, "basiapp/login.html", {'error': "user is inactive"})


        else:
            print("error1")
            return render(request, "basiapp/login.html",{'error':"invaild userid/password"})

    else:
        print("error2")
        return render(request, "basiapp/login.html")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))













def index(request):
    return render(request,"basiapp/index.html")


# Create your views here.

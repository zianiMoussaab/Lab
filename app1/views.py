from django.shortcuts import render
from django.http import HttpResponse, response
from .forms import CreateNewList, LoginList
from .models import lab
# Create your views here.


def home(request):
    return render(request, "app1/home.html")


def register(request):
    if request.method =="POST":
        form = CreateNewList(request.POST)
    
        if form.is_valid():
            n = form.cleaned_data["full_name"]
            usr = form.cleaned_data["username"]
            pas = form.cleaned_data["password"]
            cty = form.cleaned_data["city"]
            regn = form.cleaned_data["region"]
            adrs = form.cleaned_data["adress"]
            t1 = form.cleaned_data["tel"]
            t2 = form.cleaned_data["tel2"]
            em = form.cleaned_data["email"]
            
            try:
                labs = lab.objects.get(username=usr)
                context= {'form': form, 'error':'The username you entered has already been taken. Please try another username.'}
                return render(request, 'app1/register.html', context)
            except lab.DoesNotExist:
                l = lab(full_name=n, username =usr, password =pas, city =cty, region =regn,adress=adrs, telephone=t1, tel2= t2, email=em )
                l.save()

            
        return response.HttpResponseRedirect("/app1/")

    else:
        form = CreateNewList()
    return render(request,"app1/register.html", {"form":form})



def login(request):
    if request.method =="POST":

        form = LoginList(request.POST)

        if form.is_valid():
            usr = form.cleaned_data["username"]
            pas = form.cleaned_data["password"]

            try:
                labs = lab.objects.get(username=usr, password=pas)
                context= {'form':form , 'error':'Loged IN'}
                return render(request, 'app1/login.html', context)
                    
            except lab.DoesNotExist:
                context = {'form':form ,'error': 'User name or Pass doesnt exist '}
                return render(request, 'app1/login.html', context)



        else:
            context= {'form':form , 'error':'form unvalid'}
            return render(request, 'app1/login.html', context)

    else:
        form = LoginList()
        return render(request,"app1/login.html", {"form":form})
   
from django.shortcuts import render
from myapp.models import product, cat
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout



def index(request):
  name = request.session.get("is_auth","Не авторизован")
  if name != "Не авторизован":
    res = product.objects.all()
    if request.method == "POST":
      
      data = request.POST
      if data["cat"] == "form1":

        new = product(name = data["field1"], description = data["field2"], cost = data  ["field3"], count = data["field4"])
        new.save()
      elif data["cat"] == "form2":
        logout(request)
        return redirect(auth)

      return render(request,'index.html', {"prod":res,"username":name})

    else:
      
      return render(request,'index.html', {"prod":res,"username":name})
  else:
    return redirect(auth)





def auth(request):
  if request.method == "POST":
    data = request.POST
    user = authenticate(username = data["lgn"], password = data["psw"])
    if user is not None:
      request.session["is_auth"] = user.username
      return HttpResponse(f"Привет, {user.password}")
      
    else:
      return HttpResponse(f"wrong psw")
  else:
   return render(request,"auth.html")





def card(request,pr_id):
  data = product.objects.filter(id = pr_id)
  print(data)
  if data:
    return render(request,"card.html",{"res":data}) 
  else:
    return redirect(index)







#User.objects.filter(username = data["lgn"])
#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate


def reg(request):
  if request.method == "POST":
    data = request.POST
    newUser = User.objects.create_user(data["lgn"],data["eml"],data["psw"])
    newUser.save()
    return HttpResponse(f'Пользователь {data["lgn"]} успешно создан')
  else:
   return render(request,"reg.html")





# Create your views here.
#В CMD
#python -m venv env
#env\Scripts\activate 
#Вернутся в папку с проектом и выполнить установку(..\) Django
#Pip install Django (нужно проверить, что мы находимся в #нашем виртуальном окружении)
#
#Django-admin – список доступных команд
#django-admin startproject mysite – создание проекта
# python manage.py startapp myapp
#Python manage.py runserver

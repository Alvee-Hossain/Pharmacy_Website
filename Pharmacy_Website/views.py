from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core import serializers
from Pharmacy.models import EmployeePanel,InventoryPanel,Sales,Availability

def home(request):
    return render(request,'home.html')

# def userloggedin(request, user=None):
#     # if request.method=="POST":
#     #     username=request.POST['username']
#     #     password = request.POST['password']
#     #
#     # user=authenticate(username=username,password=password)
#     # if user is not None:
#     #     login(request,user)
#     #     return redirect(request,"authentication/index.html",{'username':username})
#     # else:
#     #     messages.error(request,"Bad Credentials!")
#     #     return redirect('home')
#     return render(request,'userloggedin.html')

# def register(request):
#     # if(request.method=='POST'):
#     #     form=RegistrationForm(request.POST)
#     #     if(form.is_valid()):
#     #         form.save()
#     #     return redirect('home')
#     # form=RegistrationForm()
#     # context={
#     #     'registration_form':form
#     # }
#     return render(request,'register.html')

def login(request):
    if (request.method == 'POST'):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in!")
            return redirect('/pharmacy')
        else:
            messages.error(request,"Given information is not correct!")
            return redirect('/login/')
    return render(request,'login.html')

def employee(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        number = request.POST['number']
        address = request.POST['address']
        em=EmployeePanel(username=username,password=password,number=number,address=address)
        em.save()
    return render(request,'employee.html')

def umedicinelist(request):
    return render(request,'umedicinelist.html')

def forgotpassword(request):
    return render(request,'forgotpassword.html')

def otp(request):
    return render(request,'otp.html')

def resetpassword(request):
    return render(request,'resetpassword.html')

def admin(request):
    return render(request,'admin.html')

def available(request):
    data = serializers.serialize("python", Availability.objects.all())
    context = {
        'data': data,
    }
    return render(request, 'search_drugs.html', context)

def aemployee(request):
    data=serializers.serialize("python",EmployeePanel.objects.all())
    context={
        'data':data,
    }
    return render(request,'aemployee.html',context)

def ainventory(request):
    # data = serializers.serialize("python",InventoryPanel.objects.all())
    # context = {
    #     'data': data,
    # }
    return render(request,'ainventory.html')

def asales(request):
    # data = serializers.serialize("python", Sales.objects.all())
    # context = {
    #     'data': data,
    # }
    return render(request,'asales.html')

def aprebooklists(request):
    return render(request,'aprebooklists.html')

def echeckbookeddrugs(request):
    return render(request,'echechbookeddrugs.html')

def ereciepts(request):
    return render(request,'ereciepts.html')

def echeckid(request):
    return render(request,'echeckid.html')

def logout(request):
    logout(request)
    messages.success(request,"Logged out")
    return redirect('/pharmacy')
    return HttpResponse('logout')

def search_drugs(request):
    return render(request,'search_drugs.html')

def esearchdrugs1(request):
    return render(request,'esearchdrugs1.html')

def esearchdrugs2(request):
    return render(request,'esearchdrugs2.html')

def pharmacy(request):
    return render(request,'pharmacy.html')
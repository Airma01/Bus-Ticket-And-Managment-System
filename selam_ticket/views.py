from django.shortcuts import render,redirect
from .models import SelamBusInfo
from .models import BookingTickect
from .utils import CustomerUser
from .models import Announcement
from django.contrib import messages
from django.contrib.auth import logout
from .code_verification import OTP_REQUEST
# views.py

def register(request):
    if request.method == 'POST':

        form = CustomerUser(request.POST)
        if form.is_valid():
           code = OTP_REQUEST(request.POST.get('email'))
           request.session['form_data']=request.POST
           request.session['code'] =code
           return redirect('verify')
    else:
        form = CustomerUser()
        return render(request, 'Registration.html', {'form': form})
from django.contrib.auth.models import User  # Or your custom user model

def verify(requset):
    if requset.method == 'POST':
        form_data = requset.session['form_data']
        server_code = requset.session['code']
        form_code =requset.POST.get('code')

        form = CustomerUser(form_data)
        if form.is_valid():
            if int(server_code) == int(form_code):
                form.save()
                return redirect('login')
            requset.session.pop('form_data',None)
            requset.session.pop('code',None)

    return render(requset,'verify.html')
            




def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
      Announce =Announcement.objects.all()
      BusInfo = SelamBusInfo.objects.all()
      context = {'BusInfo':BusInfo,'announce':Announce}

    return render(request,'home.html',context=context)
def logout_view(request):
    logout(request)
    return redirect('login')
def detail(request,pk):

    DetailInfo = SelamBusInfo.objects.get(pk=pk)
    context ={'detail':DetailInfo}
    return render(request,'detail_info.html',context=context)

def BookTheTicket(request,pk):
     
     bus = SelamBusInfo.objects.get(pk=pk)
     if request.method == 'POST':
         NationalId = request.FILES.get("NationalId")
         payment = request.FILES.get("payment")
         book=BookingTickect.objects.create(customer=request.user,Bus=bus,payment_method=payment,digital_id=NationalId)
         return redirect('home')
     
     return render(request,'order.html',{'bus':bus})
def my_order(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
       orders = BookingTickect.objects.filter(customer=request.user)
       
       return render(request,'my_order.html',{'order':orders})

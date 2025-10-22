"""
URL configuration for selam_bus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from .import views
urlpatterns = [

    path("userRegist",views.register,name='userRegist'),
    path("/home",views.home,name='home'),# http://127.0.0.1:8000/home
    path('logout', views.logout_view, name='logout'),
    path('detail/<int:pk>',views.detail,name='detail'), # http://127.0.0.1:8000/detail\
    path('order/<int:pk>',views.BookTheTicket,name='order'),
    path('verify',views.verify,name='verify'),
    path('my_order',views.my_order,name='my_order')
]



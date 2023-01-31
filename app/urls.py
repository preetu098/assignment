"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from pro import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('dashboard/',views.dashboard),
    path('mobile/',views.mobile),
    path('pay/',views.payment),
    path('buycoin/',views.getCoins),
    path('coins/',views.coinsform),
    path('coinstatus/',views.coinStatus),
    path('promote/',views.promote),
    path('invite/',views.invite),
    path('search/',views.searchRecord),
    path('requesttutor/',views.requestTutor),
    path('register/',views.register),
    path('assign/',views.assignmenthelp)
]

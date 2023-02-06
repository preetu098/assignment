from django.urls import path
from pro import views
urlpatterns = [
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
    path('assign/',views.assignmenthelp,name="assign")
]
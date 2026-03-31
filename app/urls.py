from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('acc_creation',views.acc_creation,name='acc_creation'),
    path('pin_generation',views.pin_generation,name='pin_generation'),
    path('pin_generation-2',views.pin_generation2,name='pin_generation2'),
    path('check_balance',views.check_balance,name='check_balance'),
    path('deposit',views.deposit,name='deposit'),
    path('withdraw',views.withdraw,name='withdraw'),
    path('transfer',views.transfer,name='transfer'),
]
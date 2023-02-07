from .views import *
from django.urls import path

urlpatterns = [
    path('',login,name = 'login'),
    path('home/',home,name='home'),
    path('man/',man,name='man'),
    path('hr/',hr_f,name='hr_f'),
    path('adminn/',adminn,name='adminn'),
    path('emp/',emp,name='emp'),
    path('hrreg',hrreg,name='hrreg'),
    path('manreg/',manreg,name='manreg'),

]

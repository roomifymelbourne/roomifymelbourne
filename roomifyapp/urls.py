from django.urls import path
from . import views
app_name='roomifyapp'

urlpatterns = [
   path('',views.home,name='home'),
   path('tandc/',views.tandc,name='tandc'),
]
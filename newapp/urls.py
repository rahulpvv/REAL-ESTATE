from django.urls import path
from newapp import views


urlpatterns = [
    path('index/',views.index,name="index")

]
"""airportproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from airport import views

urlpatterns = [
    path('register/',views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('about/', views.aboutPage, name="about"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('admin/', admin.site.urls),  
    path('CSIA/', views.CSIAPage, name="MumbaiAirport"),
    path('IGIA/', views.IGIAPage, name="DelhiAirport"),
    path('KIA/', views.KIAPage, name="BangaloreAirport"),
    path('HIA/', views.HIAPage, name="HeathrowAirport"),
    path('FIA/', views.FIAPage, name="FrankfurtAirport"),
    path('DIA/', views.DIAPage, name="DusseldorfAirport"),
    path('DBIA/', views.DBIAPage, name="DubaiAirport"),
    path('LAIA/', views.LAIAPage, name="LAAirport"),
    path('ap', views.ap),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),
    path('al',views.al),
    path('tk',views.tk),
    path('show_al',views.show_al),
    path('edit_al/<int:id>',views.edit_al),
    path('update_al/<int:id>', views.update_al), 
    path('remove/<int:id>',views.destroy_al),
    path('show_tk', views.show_tk),
    path('show_fl',views.show_fl),
    path('show_ps',views.show_ps)
]

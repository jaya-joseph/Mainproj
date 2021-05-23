from django.urls import path
from.import views


urlpatterns = [
    path('', views.admin_view, name='home'),
    path('index', views.index, name='index'),
    path('desig/', views.display_desig, name='desig'),
    path('changeacdyear/', views.dispaly_changeacdyear, name='changeacdyear'),
    path('changeacd/', views.display_changeacd, name='changeacd'),
    path('pplfacultydetails/', views.admin_pplfacultydetails, name='pplfacultydetails'),
    path('changepd/', views.admin_changepd, name='changepd'),
    path('Adminhome/', views.display_view, name='Adminhome'),
    path('login', views.login, name='login'),
]

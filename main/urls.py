from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('countries-list',views.get_data, name='countries'),
    path('countries-list/<str:letter>',views.get_letter, name='countries'),
    path('languages-list',views.get_data2, name='languages'),
    path('languages/<str:languages>/', views.get_language, name='lang'),
    path('country/<str:country>/',views.get_country, name='con')
]
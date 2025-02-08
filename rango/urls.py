from django.urls import path
from rango import views

app_name = 'rango'  # ✅ This must be here!

urlpatterns = [
    path('', views.index, name='index'),  # URL for index page
    path('about/', views.about, name='about'),  # URL for about page
]

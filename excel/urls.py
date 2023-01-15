from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index , name='home' ),
    path('show-excel', views.show_excel , name='show_excel'),
    path('save-excel', views.save_excel , name='save_excel'),
]
from django.urls import path
from . import views

app_name = 'producto'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:producto_id>/', views.detalle, name='detalle'),
    path('nuevo/', views.nuevo, name='nuevo'),
]


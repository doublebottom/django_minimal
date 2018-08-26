from django.urls import path
from . import views

urlpatterns = [
    # / --> root
    path('', views.name, name='name'),

]

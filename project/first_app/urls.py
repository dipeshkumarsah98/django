
from . import views
from django.urls import path

app_name = 'first_app'

urlpatterns = [
    path('/about/', views.About, name='index'),

]

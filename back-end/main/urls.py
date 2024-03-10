
from django.urls import path
from . import views
from .views import form_view

urlpatterns = [
    path('', views.index,name='index'),
    path('about', views.about,name='about'),
    path('add_your_tip', views.addyourtip,name='tip'),
    path('python', views.python,name='python'),
    path('java', views.java,name='java'),
    path('form', form_view, name='form_view'),
    path('signin', views.signin, name='signin'),


]
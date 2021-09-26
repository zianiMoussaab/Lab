from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns= [
    path("",views.home, name="home"),
    path("register/",views.register, name="register"),
    path("login/", views.login, name="login"),

]

urlpatterns += staticfiles_urlpatterns()
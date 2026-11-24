from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("detail/<str:name>/",views.detail,name="detail"),
    path("about/me/",views.anout_me,name="about_me"),
]

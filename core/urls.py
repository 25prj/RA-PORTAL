from django.urls import path 
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index_page),
    path("contact/", views.contact, name="contact"),
    path("about/", views.aboutpage, name="about"),

]
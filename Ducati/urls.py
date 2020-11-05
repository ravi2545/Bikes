from django.urls import path,re_path
from .views import *

urlpatterns = [
    path("Triumph_show/", Ducati_post_get.as_view()),
    path("Triumph_save/", Ducati_save.as_view()),
]
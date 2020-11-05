from django.urls import path, re_path
from .views import *


urlpatterns = [
    path("Triumph_show/", Triumph_post_get.as_view()),
    path("Triumph_save/", Trimph_save.as_view()),
]
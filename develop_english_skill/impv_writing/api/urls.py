from django.urls import path
from impv_writing.api.views import *

urlpatterns = [
    path('get-gpt-help',get_gpt_sugession),
]
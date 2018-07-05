from django.conf.urls import url
from text_summarizer import views

urlpatterns = [
    url(r'^$', views.index),
]

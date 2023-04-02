from django.urls import path
from apps.blog import views

urlpatterns = [
    path("", views.IndexPage.as_view(), name='index')
]
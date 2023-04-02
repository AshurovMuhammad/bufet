from django.urls import path
from apps.blog import views

urlpatterns = [
    path("", views.IndexPage.as_view(), name='index'),
    path("products/", views.ProductsView.as_view(), name='prod')
]
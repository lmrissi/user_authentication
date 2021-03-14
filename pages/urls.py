from django.urls import path
from .views import HomePageView, DeletePageView, DeleteView

app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("delete/", DeletePageView.as_view(), name="delete"),
    path("delete_user/", DeleteView.as_view({'post': 'delete'}), name="delete_user"),
]
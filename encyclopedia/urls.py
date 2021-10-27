from django.urls import path

from . import views

app_name = 'wiki'
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.title, name='title'),
    path("search/", views.search, name='search'),
    path("randompage/", views.random_choice, name='random_choice'),
    path("createpage/", views.create_page, name='create_page'),
    path("edit/<str:title>", views.edit, name='edit'),
    path("saveedit/", views.saveedit, name='save_edit')
    ]

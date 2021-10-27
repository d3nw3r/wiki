from django.urls import path

from . import views

app_name = 'wiki'
urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/<str:title>", views.title, name='title'),
    path("wiki/search/", views.search, name='search'),
    path("wiki/randompage/", views.random_choice, name='random_choice'),
    path("wiki/createpage/", views.create_page, name='create_page'),
    path("wiki/edit/<str:title>", views.edit, name='edit'),
    path("wiki/saveedit/", views.saveedit, name='save_edit')
    ]

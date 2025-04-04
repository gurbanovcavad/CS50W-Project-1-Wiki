from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/create/", views.create, name='create'),
    path("wiki/save", views.save, name='save'),
    path('wiki/edit/<str:title>/', views.edit, name='edit'),
    path("wiki/<str:title>/", views.open, name='open')
]

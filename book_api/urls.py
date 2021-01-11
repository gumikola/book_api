from django.urls import path

from . import views

urlpatterns = [
    path('', views.map_api),
    path('books/', views.books),
    path('books/search', views.search_books),
    path('books/<int:book_id>/', views.book),
    path('books/<int:book_id>/opinions/', views.opinions),
    path('opinions/', views.opinions),
    path('opinions/<int:opinion_id>/', views.opinion),
]

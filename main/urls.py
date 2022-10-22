from django.urls import path
from . import views


urlpatterns = [
    path('films/', views.films),
    path('films_detail/<int:id>/', views.films_detail),

]
from django.urls import path
from . import views



app_name="order"
urlpatterns = [
    path("", views.HomeView.as_view(), name='home'), 
    path("plus/", views.add_number_of_pages, name="add-number-of-pages"),
    path('minus/', views.subtract_number_of_pages, name="subtract-number-of-pages"),
]

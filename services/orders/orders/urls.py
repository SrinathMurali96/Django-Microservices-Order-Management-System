from django.urls import path
from api import views


urlpatterns = [
	path("orders/add/", views.add_order)
]

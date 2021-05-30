from django.urls import path
from api import views


urlpatterns = [
	path("emails/send/", views.email_send)
]

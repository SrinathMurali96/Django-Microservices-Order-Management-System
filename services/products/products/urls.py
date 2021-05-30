from django.urls import path
from api import views


urlpatterns = [
	path("private/categories/", views.categories),
	path("products/fetch/", views.products_fetch),
	path("products/create/", views.products_create),
	path("products/delete/", views.products_delete),
	path("products/docs/", schema_view),
]

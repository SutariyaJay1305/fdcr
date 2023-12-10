from django.urls import path

from . import views

urlpatterns = [
    path('admin/home/detail/import/', views.perform_import_view, name='admin_home_detail_perform_import'),
    path("", views.index, name="index"),
    path("verify", views.verify, name="verify"),
]
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("mission", views.mission, name="mission"),
    path("verify", views.verify, name="verify"),
    path("admin/home/datamanager/import/", views.perform_import_view, name="admin_main_datamanager_perform_import"),

]
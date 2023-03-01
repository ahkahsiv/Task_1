
from django.contrib import admin
from django.urls import path,include
from  mainapp import views
from mainapp.views import *
from rest_framework.routers import DefaultRouter


router= DefaultRouter()
router.register("school", SchoolViewSet, basename="user")
router.register("student", StudentViewSet, basename ="student")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.index),
    path("update_page/", views.update_page),
    path("update/",views.update),
    path("delete_student/",views.delete_student),
    path("add_student/", views.add_student),
    path("search/", views.search),
    path("api/", include(router.urls)),
]

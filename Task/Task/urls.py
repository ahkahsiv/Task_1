
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
    path("",views.home),
    path("update/",views.update),
    path("delete_student/<int:id>",views.delete_student),
    path("add/",views.add),
    path("add_student/", views.add_student),
    path("api/", include(router.urls))
]

from django.urls import include, path
from . import views

from rest_framework import routers


router = routers.DefaultRouter()
router.register('Direct', views.DirectionViewSet)
router.register('Doctor', views.DoctorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

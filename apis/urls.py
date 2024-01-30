from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import ToDoViewSet

router=DefaultRouter()
router.register('',ToDoViewSet,basename='todos')
urlpatterns=router.urls

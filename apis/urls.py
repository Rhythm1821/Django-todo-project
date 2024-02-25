from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import ToDoViewSet,TodoDetail

router=DefaultRouter()
router.register('',ToDoViewSet,basename='todos')
urlpatterns=[
    *router.urls,
    path('<int:pk>/',TodoDetail.as_view(),name='todo-detail')
]
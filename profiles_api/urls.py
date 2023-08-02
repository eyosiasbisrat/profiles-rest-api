from django.urls import path, include

from rest_framework.routers import DefaultRouter
from profiles_api import views

router =  DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name = 'hello-viewset')
router.register('profile', views.UserProfileViewSet)
"""we will not need to specify a name.beause we have a query object in our view set"""
urlpatterns =[
    path('hello-view/', views.HelloApiview.as_view()),
    path('',include(router.urls))

]
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
# router.register('hello-viewset',
#                 views.MyUserViewSet,
#                 basse_name='hello-viewset')
router.register('hello-viewset',
                 views.MyUserViewSet)
  
urlpatterns = [
    
    path('', include(router.urls))
]
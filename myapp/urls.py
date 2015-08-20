from django.conf.urls import url, include
from rest_framework import routers

import myapp.views as views

router = routers.DefaultRouter()

router.register(r'category', views.CategoryViewSet, base_name='category')
router.register(r'profile', views.ProfileViewSet, base_name='profile')
router.register(r'listing', views.ListingViewSet, base_name='listing')
router.register(r'user', views.UserViewSet, base_name='user')

# Wire up our API using automatic URL routing.
urlpatterns = [
    url(r'^', include(router.urls)),
]
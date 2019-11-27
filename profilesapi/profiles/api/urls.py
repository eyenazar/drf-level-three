from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles.api.views import (ProfileViewSet, 
                                ProfileStatusViewset,
                                AvatarUpdateView)

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'status', ProfileStatusViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('avatar', AvatarUpdateView.as_view(), name='avatar-update')
]
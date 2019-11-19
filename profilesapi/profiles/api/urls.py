from django.urls import path
from profiles.api.views import ProfileViewSet

profile_list = ProfileViewSet.as_view({'get': 'list'})
profile_detail = ProfileViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    path('profiles/', profile_list, name='profile-list'),
    path('profiles/<int:pk>/', profile_detail, name='profile-detail')
]
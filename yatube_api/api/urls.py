from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'api'

router_v1 = SimpleRouter()
router_v1.register('posts', views.PostViewSet, basename='posts')
router_v1.register('groups', views.GroupViewSet, basename='groups')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    views.CommentViewSet,
    basename='comments'
)
router_v1.register('follow', views.FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]

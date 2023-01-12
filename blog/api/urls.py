
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from rest_framework.authtoken import views
from blog.api.views import UserDetail, TagViewSet, PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("tags", TagViewSet)
router.register("posts", PostViewSet)

urlpatterns = [
    #path("posts/", PostList.as_view(), name="api_post_list"), we use viewsets for list and detail
    #path("posts/<int:pk>", PostDetail.as_view(), name="api_post_detail"),
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)


urlpatterns += [
    path("auth/", include("rest_framework.urls")),
]

urlpatterns += [
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token),
    path("", include(router.urls)), #for instance you can set the url for 
]                                          #path("blabla/", include(router.urls)) and it would
                                           #work as /api/v1/blabla/tags tags here is from router.register("tags", TagViewSet)
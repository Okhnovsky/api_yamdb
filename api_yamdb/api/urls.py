from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, APISignUp, APIGenToken

app_name = 'api'

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('v1/auth/signup/', APISignUp.as_view(), name='signup'),
    path('v1/auth/token/', APIGenToken.as_view(), name='gen_token'),
    path('v1/', include(router.urls)),
]

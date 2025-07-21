from django.urls import path
from .views import UserAPIView
from .views import RegisterAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('user/', UserAPIView.as_view(), name='user_api'),
    path('signup/', RegisterAPIView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

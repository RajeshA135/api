from django.urls import path
from . import views
from user.views.products import ProductAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('users/', views.UserAPIView.as_view(), name='users'),
    path('products/', ProductAPIView.as_view(), name='products'),
    path('signup/', views.SignUpAPIView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

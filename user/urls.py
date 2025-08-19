from django.urls import path
from . import views
from user.views.products import ProductAPIView
from user.views.role import RoleAPIView
from user.views.organizaiton import OrganizationView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('users/', views.UserAPIView.as_view(), name='users'),
    path('roles/',RoleAPIView.as_view(), name='roles'),
    path('Organizations/', OrganizationView.as_view(), name='products'),
    path('products/<int:pk>/', ProductAPIView.as_view(), name='product-details'),
    path('signup/', views.SignUpAPIView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

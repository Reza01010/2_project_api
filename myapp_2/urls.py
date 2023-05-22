from django.urls import path
from .views import list_2_view_api, detail_2_view_api, list_cryptocurrency_by_market_value_1_api,\
    detail_cryptocurrency_by_market_value_1_api
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('list/', list_2_view_api, name='list_2_api'),
    path('<int:pk>/', detail_2_view_api, name='detail_2_api'),
    path('list2/', list_cryptocurrency_by_market_value_1_api, name='list_1_api'),
    path('detail2/<str:pk>/', detail_cryptocurrency_by_market_value_1_api, name='detail_1_api'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]





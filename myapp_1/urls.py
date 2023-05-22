from django.urls import path
from .views import SignUpView, list_2_view, detail_2_view, list_cryptocurrency_by_market_value_1, detail_cryptocurrency_by_market_value_1

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('list/', list_2_view, name='list_2'),
    path('<int:pk>/', detail_2_view, name='detail_2'),
    path('list2/', list_cryptocurrency_by_market_value_1, name='list_1'),
    path('detail2/<str:pk>/', detail_cryptocurrency_by_market_value_1, name='detail_1'),
]

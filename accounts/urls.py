from django.urls import path
from .views import UserSearchAPIView
 
app_name = 'accounts'

urlpatterns = [
    path('', UserSearchAPIView.as_view(), name='user_search'),
]
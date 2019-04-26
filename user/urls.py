from django.urls import path
from .views import UserView 


urlpatterns = [
        path('<int:user_id>', UserView.as_view(), name='User-View'),
        path('', UserView.as_view(), name='postview')
]

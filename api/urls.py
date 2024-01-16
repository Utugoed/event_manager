#from django.conf.urls import url
from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.views import CustomTokenObtainView
from events.views import create_event, events_list, get_event
from organisations.views import OrganisationsAPIView
from users.views import CreateUserAPIView


urlpatterns = [
    path('events/', events_list, name='get_events_list'),
    path('events/create/', create_event, name='create_event'),
    path('events/<int:id>/', get_event, name='event_detail'),
    path('organisations/', OrganisationsAPIView.as_view()),
    path('register/', CreateUserAPIView.as_view()),
    path('token/', CustomTokenObtainView.as_view(), name='token-abtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
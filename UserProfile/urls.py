from django.urls import path
from UserProfile.views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
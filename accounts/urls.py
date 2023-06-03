from django.urls import path
from .views import RegisterView,Userview

urlpatterns=[
    path('register/',RegisterView.as_view()),
    path('user/',Userview.as_view()),
]
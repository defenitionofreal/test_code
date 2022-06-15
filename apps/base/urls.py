from django.urls import path
from apps.base.api import (foods_list)

app_name = 'base'

urlpatterns = [
    path('foods/', foods_list.FoodsListAPIView.as_view()),
]

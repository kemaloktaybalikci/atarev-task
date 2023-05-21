from django.urls import path
from .views import CreateUserView, ListUsersView

urlpatterns = [
    path('user/', CreateUserView.as_view(), name='create_user'), 
    path('user/list', ListUsersView.as_view(), name='list_users')
]
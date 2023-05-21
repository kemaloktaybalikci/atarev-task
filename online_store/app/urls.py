from app.api.user.urls import urlpatterns as user_urls
from app.api.category.urls import urlpatterns as category_urls

app_name = "app"
urlpatterns = [
    *user_urls,
    *category_urls
]

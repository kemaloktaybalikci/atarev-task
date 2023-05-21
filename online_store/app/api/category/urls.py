from django.urls import path
from .views import CreateCategoryView, ListCategoriesView, GetUpdateDeleteCategoryView

urlpatterns = [
    path('category/', CreateCategoryView.as_view(), name='create_category'), 
    path('category/list', ListCategoriesView.as_view(), name='list_categories'), 
    path('category/<int:category_id>',GetUpdateDeleteCategoryView.as_view(),name='read_update_delete_category')
]
from django.urls import path
from shop.views import ItemListView, ItemDetailView, NewItem, DeleteItem

urlpatterns = [
    path('', ItemListView.as_view(), name='item-list-page'),
    path('listings/<str:slug>', ItemDetailView.as_view(), name='shop-details-page'),
    path('new/', NewItem.as_view(),name='item-create'),
    path('listings/<str:slug>/delete', DeleteItem.as_view(), name='delete-item' )
]

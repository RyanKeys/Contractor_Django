from django.urls import path
from shop.views import ItemListView, ItemDetailView

urlpatterns = [
    path('', ItemListView.as_view(), name='item-list-page'),
    path('listings/<str:slug>', ItemDetailView.as_view(), name='shop-details-page'),
]

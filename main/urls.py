from django.urls import path
from main.apps import MainConfig
from main.views import ItemCreateAPIView, ItemListAPIView, \
    ItemRetrieveAPIView, ItemDestroyAPIView

app_name = MainConfig.name

urlpatterns = [
    path('item/create/', ItemCreateAPIView.as_view(), name='item-create'),
    path('item/', ItemListAPIView.as_view(), name='item-list'),
    path('item/<int:pk>/', ItemRetrieveAPIView.as_view(),
         name='item-detail'),
    path('item/delete/<int:pk>/', ItemDestroyAPIView.as_view(),
         name='item-delete'),
]

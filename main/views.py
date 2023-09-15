from rest_framework import generics

from main.paginators import ItemPaginator
from main.services import total_price
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from main.models import Item
from main.serializers import ItemSerializer

class ItemCreateAPIView(generics.CreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = [IsAdminUser]


    def perform_create(self, serializer):
        data = self.request.data
        price = float(data['price'])
        final_price = total_price(price)
        print(final_price)
        serializer.save(final_price=final_price)


class ItemListAPIView(generics.ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    pagination_class = ItemPaginator
    permission_classes = [IsAuthenticated]


class ItemRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class ItemDestroyAPIView(generics.DestroyAPIView):
    queryset = Item.objects.all()
    permission_classes = [IsAdminUser]

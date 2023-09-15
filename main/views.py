from rest_framework import generics
from main.services import total_price

from main.models import Item
from main.serializers import ItemSerializer

class ItemCreateAPIView(generics.CreateAPIView):
    serializer_class = ItemSerializer


    def perform_create(self, serializer):
        data = self.request.data
        price = float(data['price'])
        final_price = total_price(price)
        print(final_price)
        serializer.save(final_price=final_price)


class ItemListAPIView(generics.ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class ItemRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class ItemDestroyAPIView(generics.DestroyAPIView):
    queryset = Item.objects.all()

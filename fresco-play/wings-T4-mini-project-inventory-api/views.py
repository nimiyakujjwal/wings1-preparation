from rest_framework import viewsets
from rest_framework.view import APIView
from rest_framework.response import Response
from inventoryapp.serializers import ItemSerializer
from rest_framework import status
from .model import Item

class ItemView(APIView):
    def get(self, request):
        items = Item.objects.all().order_by("-price")
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    
class QueryItemView(APIView):
    def get(self, request, category):
        items = item.objects.filter(category=category)
        serializer = ItemSerializer(items, many=True)

class InventoryItemView(APIView):
    def get(self, request):
        items = item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return response(serializer.data)
    
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            barcode = serializer.validated_data["barcode"]
            if Item.objects.filter(barcode=barcode).exists():
                return Response({"barcode":["Item with this barcode already exists."]}, status = status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_400_NOT_FOUND)
        Item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
            
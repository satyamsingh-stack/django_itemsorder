from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class inventoryItem(APIView):
    def post(self,request):
        serializers=itemSerializer(data=request.data)
        if(serializers.is_valid()):
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response({"message: Something went wrong"},status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        item=items.objects.all()
        serializer=itemSerializer(item,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def delete(self,request,barcode):
        try:
            item=items.objects.get(barcode=barcode)
        except items.DoesNotExist:
            return Response({"message: No item Found"},status=status.HTTP_404_NOT_FOUND)
        item.delete()
        return Response({"message: deleted"},status=status.HTTP_204_NO_CONTENT)
    
    def put(self,request,barcode):
        item=items.objects.filter(barcode=barcode).first()
        if(item is not None):
            serializer=itemSerializer(item,data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response({"message: updated"},status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)
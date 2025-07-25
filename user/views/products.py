from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from ..models.products import Product
from ..serializers.products import ProductSerializer
from django.shortcuts import get_object_or_404
# from rest_framework.permissions import IsAuthenticated
# from user.permissions import IsOwnerOrReadOnly


class ProductAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk=None):
        if pk is not None:
            product = get_object_or_404(Product, pk=pk, created_by=request.user)
            serializer = ProductSerializer(product)
        else:
            products = Product.objects.filter(created_by=request.user)
            serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response({"data":serializer.data, "message":"Product added successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        try:
            product = Product.objects.get(pk=pk, created_by=request.user)
        except Product.DoesNotExist:
            return Response({"error": "Not found"}, status=404)

        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data,"message":"Product Updated Successfully"})
        return Response(serializer.errors, status=400)
    def put(self, request, pk):
            product = get_object_or_404(Product, pk=pk, created_by=request.user)
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save(created_by=request.user)  # Reassign user for security
                return Response({
                    "data": serializer.data,
                    "message": "Entire Product details are updated successfully"
                }, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk, created_by=request.user)
        except Product.DoesNotExist:
            return Response({"error": "Not found"}, status=404)

        product.delete()
        return Response({"message": "Deleted successfully"}, status=204)
    
    
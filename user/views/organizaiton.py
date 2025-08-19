from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from ..models.organization import Organization
from ..serializers.organization import OrganizationSerializer
from django.shortcuts import get_object_or_404
from user.permissions import IsOwnerOrReadOnly

class OrganizationView(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    def get(self, request, pk=None):
        if pk is not None:
            organization = get_object_or_404(Organization, pk=pk, created_by=request.user)
            serializer = OrganizationSerializer(organization)
        else:
            organizations = Organization.objects.filter(created_by=request.user)
            serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response({"data":serializer.data, "message":"Organization added successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        try:
            organization = Organization.objects.get(pk=pk, created_by=request.user)
        except Organization.DoesNotExist:
            return Response({"error": "Not found"}, status=404)

        serializer = OrganizationSerializer(organization, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data,"message":"Organization Updated Successfully"})
        return Response(serializer.errors, status=400)
    def put(self, request, pk):
            product = get_object_or_404(Organization, pk=pk, created_by=request.user)
            serializer = OrganizationSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save(created_by=request.user)  # Reassign user for security
                return Response({
                    "data": serializer.data,
                    "message": "Entire Organizaton details are updated successfully"
                }, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            product = Organization.objects.get(pk=pk, created_by=request.user)
        except Organization.DoesNotExist:
            return Response({"error": "Not found"}, status=404)

        product.delete()
        return Response({"message": "Organization Deleted successfully"}, status=204)
    
    
from ..models.roles import Role
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.role import RoleSerializer
from django.shortcuts import get_object_or_404

class RoleAPIView(APIView):
    #permission_classes = [IsOwnerOrReadOnly]
    def get(self, request):
        users = Role.objects.all()
        serializer = RoleSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        print("Post method hits..")
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        user = get_object_or_404(Role, id=request.data.get('id'))
        serializer = RoleSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        user = get_object_or_404(Role, id=request.data.get('id'))
        serializer = RoleSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = get_object_or_404(Role, id=request.data.get('id'))
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

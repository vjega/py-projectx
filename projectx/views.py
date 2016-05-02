from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from projectx.models import Menus
from projectx.serializers import MenuSerializer

@api_view(['GET', 'POST'])
def menu_list(request):
    """
    List all Menus, or create a new snippet.
    """
    if request.method == 'GET':
        menu = Menus.objects.all()
        serializer = MenuSerializer(menu, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
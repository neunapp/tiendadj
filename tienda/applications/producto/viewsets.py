from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated, AllowAny
#
from .models import Product, Colors
#
from .serializers import (
    ColorsSerializer,
    PaginationSerializer,
    ProductSerializer,
    ProductSerializerViewSet
)


class ColorViewSet(viewsets.ModelViewSet):
    """
    
    """
    serializer_class = ColorsSerializer
    queryset = Colors.objects.all()
    pagination_class = PaginationSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """  """
    serializer_class = ProductSerializerViewSet
    queryset = Product.objects.all()
    pagination_class = PaginationSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if (self.action == 'list') or (self.action == 'retrieve'):
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(
            video="https://youtu.be/h8a1gLl9C5A"
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        #
        headers = self.get_success_headers(serializer.data)
        # solo como ejemplo de que se puede escribir codigo
        respuesta = {
            'code': 'ok',
            'mensaje': 'todo correcto',
            'producto': serializer.validated_data['name'],
        }
        return Response(respuesta, status=status.HTTP_201_CREATED, headers=headers)
    
    
    def list(self, request, *args, **kwargs):
        usuario = self.request.user
        queryset = Product.objects.productos_por_user(usuario)

        # ******** esta parte las borramos *******
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
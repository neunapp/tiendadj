# apps de terceros
from rest_framework.generics import (
    ListAPIView,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
#
from django.shortcuts import render

# local models
from .models import Product
# local serialiozers
from .serializers import ProductSerializer


class ListProductoUser(ListAPIView):
    """ vista para listar prosuctos por usuario creador """
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated] # ReadOnly, IsAdminUser

    def get_queryset(self):
        #
        usuario = self.request.user
        print('**********usurio por token***********')
        print(usuario)
        return Product.objects.productos_por_user(usuario)


class ListProductoStok(ListAPIView):
    """
        Vista para lista productos con stok mayor a cero
    """
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        return Product.objects.productos_con_stok()



class ListProductoGenero(ListAPIView):
    """
        Vista para lista productos por genero
    """
    serializer_class = ProductSerializer

    def get_queryset(self):
        genero = self.kwargs['gender']        
        return Product.objects.productos_por_genero(genero)


class FiltrarProductos(ListAPIView):
    """
        Vista que lista procutos en base a varios filtros
    """
    serializer_class = ProductSerializer

    def get_queryset(self):    
        varon = self.request.query_params.get('man', None)
        mujer = self.request.query_params.get('woman', None)
        nombre = self.request.query_params.get('name', None)
        #
        return Product.objects.filtrar_productos(
            man=varon, 
            woman=mujer, 
            name=nombre
        )




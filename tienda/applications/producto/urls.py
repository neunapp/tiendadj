# django
from django.urls import include, re_path, path

# local
from . import views

app_name="producto_app"

urlpatterns = [
    # lista productos por usuario
    path(
        'api/product/por-usuario/',
        views.ListProductoUser.as_view(),
        name='product-producto_by_user'
    ),
    # lista productos con stok > 0
    path(
        'api/product/con-stok/',
        views.ListProductoStok.as_view(),
        name='product-producto_con_stok'
    ),
    # lista productos por genero
    path(
        'api/product/por-genero/<gender>/',
        views.ListProductoGenero.as_view(),
        name='product-producto_por_genero'
    ),
    # lista productos por genero
    path(
        'api/product/filtrar/',
        views.FiltrarProductos.as_view(),
        name='product-filtrar'
    ),
]
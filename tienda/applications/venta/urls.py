# django
from django.urls import include, re_path, path

# local
from . import views

app_name="venta_app"

urlpatterns = [
    # proceso de venta
    path(
        'api/venta/reporte/',
        views.ReporteVentasList.as_view(),
        name='venta-reporte'
    ),
    # proceso de venta
    path(
        'api/venta/create/',
        views.RegistrarVenta.as_view(),
        name='venta-register'
    ),
    # proceso de venta 2
    path(
        'api/venta/add/',
        views.RegistrarVenta2.as_view(),
        name='venta-register2'
    ),
]

from django.urls import path, include
from rest_framework import routers
from . import viewsets
 
router = routers.DefaultRouter()
router.register(r'tiponecesidad', viewsets.TipoNecesidadViewSet)
router.register(r'tiporeporte', viewsets.TipoReporteViewSet)
router.register(r'reportecovid', viewsets.ReporteCovidViewSet)
router.register(r'ubicacionescovid', viewsets.UbicacionesCovidViewSet)
router.register(r'reportenecesidad', viewsets.ReporteNecesidadViewSet)
router.register(r'ubicacionesnecesidad', viewsets.UbicacionesNecesidadViewSet)


urlpatterns = [
    path(r'', include(router.urls))
]
from datetime import datetime, timedelta
from . import models
from backend.apps.utils.serializers import CustomSerializer
from rest_framework import serializers

class TipoNecesidadSerializer(CustomSerializer):

    class Meta:
        model = models.Pedido
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
        ]

class TipoReporteSerializer(CustomSerializer):
    
    class Meta:
        model = models.Pedido
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
        ]

class UbicacionesCovidSerializer(CustomSerializer):
    
    class Meta:
        model = models.Pedido
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
        ]

class ReporteNecesidadSerializer(CustomSerializer):
    
    class Meta:
        model = models.Pedido
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
        ]

class UbicacionesNecesidadSerializer(CustomSerializer):
    
    class Meta:
        model = models.Pedido
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
        ]

class ReporteCovidSerializer(CustomSerializer):
    
    class Meta:
        model = models.Pedido
        exclude = [
            'archived',
            'created',
            'updated',
        ]
        extra_fields = [
        ]
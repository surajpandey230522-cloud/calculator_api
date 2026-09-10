from rest_framework.serializers import ModelSerializer
from .models import Calculation

class CalculatorSerializer(ModelSerializer):
    class Meta:
        model=Calculation
        fields='__all__'
        read_only_fields=['created_on']
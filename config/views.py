from rest_framework.views import APIView
from .serializers import CalculatorSerializer
from core.models import Calculation
from rest_framework.response import Response

class CalculationAPI(APIView):
    def get(self, request):
        data=Calculation.objects.all()
        serial=CalculatorSerializer(data, many=True)
        return Response(serial.data, status=200)

    def post(self, request):
        serial=CalculatorSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=201)
        return Response(serial.errors, status=400)
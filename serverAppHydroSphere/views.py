from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import get_predicted_aquatic_environment
from .serializers import AquaticEnvironmentPredictionSerializer

class PredictAquaticEnvironmentView(APIView):
    def post(self, request):
        serializer = AquaticEnvironmentPredictionSerializer(data=request.data)
        if serializer.is_valid():
            dissolved_oxygen = serializer.validated_data['dissolved_oxygen']
            salinities = serializer.validated_data['salinities']

            prediction = get_predicted_aquatic_environment(dissolved_oxygen, salinities)
            return Response({'prediction': prediction}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

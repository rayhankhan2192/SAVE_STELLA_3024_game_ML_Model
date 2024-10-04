from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import LandTypePredictionSerializer
import numpy as np
import pickle
import json

__model = None
__data_columns = None

def load_saved_artifacts():
    global __data_columns
    global __model

    with open('E:\\Python\\Machile Learning\\Nasa Space App\\Game Model\\server\\serverAppAtmosphere\\artifacts_Atmos\\columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']

    if __model is None:
        with open('E:\\Python\\Machile Learning\\Nasa Space App\\Game Model\\server\\serverAppAtmosphere\\artifacts_Atmos\\atmosphere_model.pickle', 'rb') as f:
            __model = pickle.load(f)

def get_predicted_land_type(air_temp, aerosols):
    if air_temp < -10 or air_temp > 50:
        return 'Invalid air temperature value'
    if aerosols < -999 or aerosols > 4:
        return 'Invalid aerosols value'

    x = np.array([air_temp, aerosols]).reshape(1, -1)
    predicted_index = __model.predict(x)[0]  # Adjust this based on your model's output type
    return predicted_index

class PredictLandTypeView(APIView):
    def post(self, request):
        serializer = LandTypePredictionSerializer(data=request.data)
        if serializer.is_valid():
            air_temp = serializer.validated_data['air_temp']
            aerosols = serializer.validated_data['aerosols']
            prediction = get_predicted_land_type(air_temp, aerosols)

            return Response({'prediction': prediction}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Load artifacts on module import
load_saved_artifacts()

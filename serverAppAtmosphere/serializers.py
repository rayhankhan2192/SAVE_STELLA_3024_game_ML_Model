from rest_framework import serializers

class LandTypePredictionSerializer(serializers.Serializer):
    air_temp = serializers.FloatField()
    aerosols = serializers.FloatField()

from rest_framework import serializers

class AquaticEnvironmentPredictionSerializer(serializers.Serializer):
    dissolved_oxygen = serializers.FloatField()
    salinities = serializers.FloatField()

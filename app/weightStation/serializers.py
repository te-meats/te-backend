from rest_framework import serializers

class LiveWeightSerializer(serializers.Serializer):
    liveWeight = serializers.FloatField
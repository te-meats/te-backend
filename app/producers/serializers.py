from rest_framework import serializers
from producers.models import Producer

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'
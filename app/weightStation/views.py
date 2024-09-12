from django.http import Http404
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from weightStation.serializers import LiveWeightSerializer

# Create your views here.
class LiveWeight(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        # Implement listener on COM port
        liveWeight = 123.51
        # serializer = LiveWeightSerializer(liveWeight)

        return Response({ 'live_weight': liveWeight })
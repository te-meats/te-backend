from django.http import Http404
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cuttingInstructions.models import CuttingInstruction, Primal, Cut
from cuttingInstructions.serializers import CuttingInstructionSerializer


# Create your views here.
class CuttingInstructionList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return CuttingInstruction.objects.get(pk=pk)
        except CuttingInstruction.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        cutting_instructions = CuttingInstruction.objects.all()
        serializer = CuttingInstructionSerializer(cutting_instructions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CuttingInstructionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        cutting_instruction = self.get_object(pk)
        serializer = CuttingInstructionSerializer(cutting_instruction, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        producer = self.get_object(pk)
        producer.delete()
        return Response(pk, status=status.HTTP_204_NO_CONTENT)

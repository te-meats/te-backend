from rest_framework import serializers
from cuttingInstructions.models import CuttingInstruction, Primal, Cut


class CutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cut
        fields = '__all__'


class PrimalSerializer(serializers.ModelSerializer):
    cuts = CutSerializer(many=True)

    class Meta:
        model = Primal
        fields = '__all__'


class CuttingInstructionSerializer(serializers.ModelSerializer):
    primals = PrimalSerializer(many=True)

    class Meta:
        model = CuttingInstruction
        fields = '__all__'

    def create(self, validated_data):
        primals = validated_data.pop('primals')
        cut_sheet = CuttingInstruction.objects.create(**validated_data)
        for primal in primals:
            cuts = primal.pop('cuts')
            primal_obj = Primal.objects.create(name=primal['name'], cutting_instruction=cut_sheet)
            for cut in cuts:
                Cut.objects.create(primal=primal_obj, name=cut['name'], cutType=cut['cutType'],
                                   prepType=cut['prepType'],
                                   quantity=cut['quantity'])
        return cut_sheet

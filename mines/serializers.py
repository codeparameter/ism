from rest_framework import serializers

from .models import Material, Mine

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = (
            'id',
            'name',
        )

class MineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mine
        fields = (
            'id',
            'name',
            'city',
            'material',
            'adr',
            'phone',
        )

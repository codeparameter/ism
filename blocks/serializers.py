from rest_framework import serializers

from .models import *

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = (
            'name',
        )

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = (
            'name',
        )

class SchemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schema
        fields = (
            'name',
        )

class QualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quality
        fields = (
            'grade',
        )

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = (
            'city',
            'city_name',
            'material',
            'material_name',
            'schema',
            'schema_name',
            'quality',
            'length',
            'height',
            'width',
            'available',
        )
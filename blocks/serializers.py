from rest_framework import serializers

from .models import *

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = (
            'id',
            'name',
        )

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = (
            'id',
            'name',
        )

class SchemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schema
        fields = (
            'id',
            'name',
        )

class QualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quality
        fields = (
            'id',
            'grade',
        )

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = (
            'id',
            'city',
            'city_name',
            'material',
            'material_name',
            'schema',
            'schema_name',
            'quality',
            'quality_name',
            'length',
            'height',
            'width',
            'not_available',
        )
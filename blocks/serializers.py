from rest_framework import serializers
from rest_framework.reverse import reverse

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
    url = serializers.SerializerMethodField(read_only=True)
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
            'created_at',
            'url',
        )

    
    def get_url(self, obj):
        request = self.context.get('request') # self.request
        if request is None:
            return None
        return reverse('blocks-detail', kwargs={"pk": obj.pk}, request=request)
        # blocks-detail is a name created by router from the basename

class BlockPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockPic
        fields = (
            'id',
            'block',
            'pic',
        )

class BlockVidSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockVid
        fields = (
            'id',
            'block',
            'vid',
        )
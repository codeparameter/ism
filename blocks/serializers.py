from rest_framework import serializers
from rest_framework.reverse import reverse

from home.settings import media_url

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
    pics = serializers.SerializerMethodField(read_only=True)
    vids = serializers.SerializerMethodField(read_only=True)
    # main_pic = serializers.SerializerMethodField(read_only=True)
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
            'url',
            'pics',
            'vids',
            # 'main_pic',
            'created_at',
        )
    
    def get_url(self, obj):
        request = self.context.get('request') # self.request
        if request is None:
            return None
        return reverse('blocks-detail', kwargs={"pk": obj.pk}, request=request)
        # blocks-detail is a name created by router from the basename
    
    def get_pics(self, obj):
        return obj.pics
    
    def get_vids(self, obj):
        return obj.vids
    
    # def get_main_pic(self, obj):
    #     request = self.context.get('request') # self.request
    #     default_pic = BlockPic.objects.filter(block__pk=obj.pk).order_by('-default', 'priority', '-pk').first()
    #     print(f'{BlockPic.objects.filter(block__pk=obj.pk).order_by('-default', 'priority', '-pk').all()}')
    #     return media_url(request, default_pic.pic) if \
    #             default_pic else \
    #             null
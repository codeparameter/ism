from rest_framework import serializers
from rest_framework.reverse import reverse

from home.settings import media_url

from .models import Schema, Quality, Block

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
    class Meta:
        model = Block
        fields = (
            'id',
            'mine',
            # 'city',
            # 'city_name',
            # 'material',
            # 'material_name',
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
            'created_at',
        )
    
    def get_url(self, obj):
        request = self.context.get('request') # self.request
        if request is None:
            return None
        return reverse('blocks-detail', kwargs={"pk": obj.pk}, request=request)
        # blocks-detail is a name created by router from the basename
    
    def get_pics(self, obj):
        request = self.context.get('request') # self.request
        return [{**pic, 'url': media_url(request, pic['url'])} for pic in obj.pics]
            
    
    def get_vids(self, obj):
        request = self.context.get('request') # self.request
        return [{**vid, 'url': media_url(request, vid['url'])} for vid in obj.vids]
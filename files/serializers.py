from rest_framework import serializers

from .models import *

class PicSerializer(serializers.ModelSerializer):
    dependencies = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Pic
        fields = (
            'id',
            'dependencies',
            'pic',
        )
    
    def get_dependencies(self, obj):
        return obj.dependencies

class VidSerializer(serializers.ModelSerializer):
    dependencies = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Vid
        fields = (
            'id',
            'dependencies',
            'vid',
        )
    
    def get_dependencies(self, obj):
        return obj.dependencies
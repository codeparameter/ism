from rest_framework import serializers

from .models import Material, Activity, Mine, MineStaff

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = (
            'id',
            'name',
        )

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = (
            'id',
            'status',
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
            'ph_no',
            'activity',
        )

class MineStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = MineStaff
        fields = (
            'id',
            'user',
            'mine',
        )

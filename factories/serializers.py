from rest_framework import serializers

from .models import Activity, Factory, FactoryStaff

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = (
            'id',
            'status',
        )

class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = (
            'id',
            'name',
            'city',
            'adr',
            'ph_no',
            'activity',
            'contact_info',
        )

class FactoryStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryStaff
        fields = (
            'id',
            'user',
            'mine',
        )

import django_filters

from cities.models import City
from mines.models import Material, Mine
from .models import Availability, Block, Color, Quality, Schema

from datetime import datetime

class CustomDateRangeFilter(django_filters.Filter):
    def filter(self, qs, value):
        if not value:
            return qs
            
        start_date, end_date = value.split(',')
        filter_kwargs = {}

        if start_date:
            start_date = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S.%fZ")
            filter_kwargs[f"{self.field_name}__gte"] = start_date
        if end_date:
            end_date = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%S.%fZ")
            filter_kwargs[f"{self.field_name}__lte"] = end_date

        return qs.filter(**filter_kwargs)

class BlockFilter(django_filters.FilterSet):

    mine = django_filters.ModelMultipleChoiceFilter(
        field_name='mine_id',
        queryset=Mine.objects.all(),
        to_field_name='id',
        )
    mtr = django_filters.ModelMultipleChoiceFilter(
        field_name='mtr_id',
        queryset=Material.objects.all(),
        to_field_name='id',
        )
    ct = django_filters.ModelMultipleChoiceFilter(
        field_name='ct_id',
        queryset=City.objects.all(),
        to_field_name='id',
        )
    color = django_filters.ModelMultipleChoiceFilter(
        field_name='color_id',
        queryset=Color.objects.all(),
        to_field_name='id',
        )
    schema = django_filters.ModelMultipleChoiceFilter(
        field_name='schema_id',
        queryset=Schema.objects.all(),
        to_field_name='id',
        )
    quality = django_filters.ModelMultipleChoiceFilter(
        field_name='quality_id',
        queryset=Quality.objects.all(),
        to_field_name='id',
        )
    availability = django_filters.ModelMultipleChoiceFilter(
        field_name='availability_id',
        queryset=Availability.objects.all(),
        to_field_name='id',
        )
    length = django_filters.RangeFilter()
    height = django_filters.RangeFilter()
    width = django_filters.RangeFilter()
    created_at = CustomDateRangeFilter(field_name='created_at')
    
    class Meta:
        model = Block
        fields = [
            'mine', 
            'mtr', 
            'ct',
            'color',
            'schema',
            'quality',
            'length',
            'height',
            'width',
            'created_at',
            ]
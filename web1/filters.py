import django_filters
from .models import *
from django_filters import DateFilter,CharFilter
class OrderFilter(django_filters.FilterSet):
    start = DateFilter(field_name='date_created',lookup_expr='gte')
    end = DateFilter(field_name='date_created', lookup_expr='lte')
    note = CharFilter(field_name='note',lookup_expr='icontains')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer','date_created']

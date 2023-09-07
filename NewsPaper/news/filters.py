from django_filters import FilterSet, DateFilter, CharFilter, ModelChoiceFilter
from .models import Category
from django.forms import DateInput


class NewsFilter(FilterSet):
    date = DateFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Дата',
        widget=DateInput(
            format='%d-%m-%Y',
            attrs={'type': 'date'},
        ),
    )

    name = CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Название'
    )

    category = ModelChoiceFilter(
        field_name='postCategory',
        queryset=Category.objects.all(),
        label='Категория',
        empty_label='Все'
    )

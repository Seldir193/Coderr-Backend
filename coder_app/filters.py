from django_filters import rest_framework as filters
from coder_app.models import Offer
from django.db.models import Q

class OfferFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")
    max_delivery_time = filters.NumberFilter(field_name="delivery_time_in_days", lookup_expr="lte")
    search = filters.CharFilter(method="filter_search")

    class Meta:
        model = Offer
        fields = ["min_price","max_price","max_delivery_time",'price']

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) | Q(description__icontains=value)
        )

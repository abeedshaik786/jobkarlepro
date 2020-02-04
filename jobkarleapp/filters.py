import django_filters
from .models import JobRequirments

class snippetFilter(django_filters.FilterSet):
    class Meta:
        model = JobRequirments
        fields = ('Skills','Interview_Location')
from .models import make1
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = make1
        fields = ['car_make' ]
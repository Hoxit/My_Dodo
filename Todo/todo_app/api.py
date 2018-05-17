from tastypie.resources import ModelResource
from .models import WorkToday


class WorkTodayResource(ModelResource):
    class Meta:
        queryset = WorkToday.objects.all()
        resource_name = 'work'
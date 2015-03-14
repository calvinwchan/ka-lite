from tastypie.resources import ModelResource
from .models import *

class TopicTreeResource(ModelResource):
	class Meta:
		queryset = TopicTree.objects.all()
		resource_name = 'topictree'
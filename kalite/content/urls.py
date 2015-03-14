from django.conf import settings
from django.conf.urls import include, patterns, url

from .api_resources import *

topictree_resource = TopicTreeResource()

urlpatterns = patterns(__package__ + '.views',
    url(r'^', 'content_view', {}, 'content_view'),
    url(r'^api/', include(topictree_resource.urls)),
)
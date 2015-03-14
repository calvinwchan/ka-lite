from django.contrib import admin

from .models import *


'''class TopicTreeAdmin(admin.ModelAdmin):
    list_display = ('name', 'root_node',)
admin.site.register(TopicTree, TopicTreeAdmin)

class NodeDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'created',)
admin.site.register(NodeData, NodeDataAdmin)

class NodeAdmin(admin.ModelAdmin):
    list_display = ('published', 'deleted',)
admin.site.register(Node, NodeAdmin)

class DraftAdmin(admin.ModelAdmin):
    list_display = ('publish_in',)
admin.site.register(Draft, DraftAdmin)

class ContentAdmin(admin.ModelAdmin):
    list_display = ('author', 'license_owner',)
admin.site.register(Content, ContentAdmin)

class ContentVideoAdmin(admin.ModelAdmin):
    list_display = ('video_file',)
admin.site.register(ContentVideo, ContentVideoAdmin)

class ContentVideoNodeAdmin(admin.ModelAdmin):
    pass
admin.site.register(ContentVideoNode, ContentVideoNodeAdmin)

class ContentVideoDraftAdmin(admin.ModelAdmin):
    pass
admin.site.register(ContentVideoDraft, ContentVideoDraftAdmin)

class ContentPDFNodeAdmin(admin.ModelAdmin):
    pass
admin.site.register(ContentPDFNode, ContentPDFNodeAdmin)

class ContentPDFDraftAdmin(admin.ModelAdmin):
    pass
admin.site.register(ContentPDFDraft, ContentPDFDraftAdmin)

class ExerciseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Exercise, ExerciseAdmin)

class ExerciseNodeAdmin(admin.ModelAdmin):
    pass
admin.site.register(ExerciseNode, ExerciseNodeAdmin)'''

class ExerciseDraftAdmin(admin.ModelAdmin):
    pass
admin.site.register(ExerciseDraft, ExerciseDraftAdmin)

class ContentLicenseAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(ContentLicense, ContentLicenseAdmin)
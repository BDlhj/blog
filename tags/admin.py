from django.contrib import admin
from tags.models import Tag, TagCommentSet, TagPostSet


admin.site.register(Tag)
admin.site.register(TagCommentSet)
admin.site.register(TagPostSet)

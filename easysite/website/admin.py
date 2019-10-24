from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import SiteInfo, SiteTag, VisitLog, MediaImage, SiteContents


# Register your models here.

class Content(admin.TabularInline):
	model = SiteContents
	extra = 3
	formfield_overrides = {
		models.TextField: {'widget': Textarea(
			attrs={'rows': 2,
			       'cols': 100,
			       'style': 'height: 2em;'})},
	}


class ImageInline(admin.TabularInline):
	model = MediaImage
	extra = 1


class Site(admin.ModelAdmin):
	formfield_overrides = {
		models.TextField: {'widget': Textarea(
			attrs={'rows': 1, 'cols': 40, 'style': 'height: 1em;'})},
	}
	fields = ['title', 'subtitle', 'caption', 'tags']
	list_display = ['title', 'get_tags', 'caption']
	inlines = [ImageInline, Content]


admin.site.register(SiteInfo, Site)
admin.site.register(SiteTag)
admin.site.register(VisitLog)
admin.site.register(MediaImage)

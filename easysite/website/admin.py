from django.contrib import admin

from .models import SiteInfo, SiteTag, VisitLog, MediaImage


# Register your models here.

class WebSiteInfo(admin.ModelAdmin):
	pass


class Log(admin.ModelAdmin):
	pass


admin.site.register(SiteInfo, WebSiteInfo)
admin.site.register(SiteTag, WebSiteInfo)
admin.site.register(VisitLog, Log)
admin.site.register(MediaImage, Log)

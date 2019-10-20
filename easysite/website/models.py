from django.db import models
from django.utils import timezone


# Create your models here.

class SiteInfo(models.Model):
	title = models.CharField(max_length=30, null=True)
	thumbnail = models.ForeignKey('MediaImage', on_delete=models.CASCADE, blank=True)
	index = models.TextField(blank=True)
	content = models.TextField(blank=True)
	date = models.DateField(default=timezone.now)
	tags = models.ManyToManyField('SiteTag', blank=True)
	count = models.IntegerField(default=0)

	def __str__(self):
		return self.title


class SiteTag(models.Model):
	tag_name = models.CharField(max_length=10, unique=True, name='tag_name')
	tag_info = models.TextField(null=True)
	count = models.IntegerField(default=0)

	def __str__(self):
		return self.tag_name


class VisitLog(models.Model):
	date = models.DateField(default=timezone.now)
	place = models.ForeignKey('SiteInfo', on_delete=models.CASCADE)

	def __str__(self):
		name = str(self.place) + " - " + str(self.date)
		return name


class MediaImage(models.Model):
	tag = models.CharField(max_length=20, blank=True)
	attach = models.FileField(
		upload_to='uploads/%Y/%m/%d/',
		verbose_name='添付ファイル',
	)
	date = models.DateField(default=timezone.now)

	def __str__(self):
		return self.tag

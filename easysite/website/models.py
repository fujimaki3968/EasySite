from django.db import models
from django.utils import timezone


# Create your models here.

class SiteInfo(models.Model):
	title = models.CharField(max_length=15, null=True, unique=True)
	subtitle = models.CharField(max_length=40, null=True)
	thumbnail = models.ImageField(
		upload_to='uploads/thumbnail/%Y/%m/%d/',
		verbose_name='サムネイル',
		null=True,
		blank=True
	)
	caption = models.TextField(max_length=150, null=True)
	date = models.DateField(default=timezone.now)
	tags = models.ManyToManyField('SiteTag', blank=True)
	count = models.IntegerField(default=0)

	def __str__(self):
		return self.title

	def get_tags(self):
		return ",".join([str(p) for p in self.tags.all()])

	class Meta:
		ordering = ['-date']


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
	site_info = models.ForeignKey('SiteInfo', on_delete=models.CASCADE, blank=True, null=True)
	attach = models.FileField(
		upload_to='uploads/%Y/%m/%d/',
		verbose_name='添付ファイル',
	)

	def __str__(self):
		name = self.attach.name
		return name


class SiteContents(models.Model):
	site_info = models.ForeignKey('SiteInfo', on_delete=models.CASCADE, null=True)
	index = models.CharField(max_length=20, null=True)
	content = models.TextField(null=True)
	img_type = models.IntegerField(default=0)
	image = models.ForeignKey('MediaImage', on_delete=models.CASCADE, blank=True, null=True)

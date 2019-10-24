from django.shortcuts import render, get_object_or_404

from .models import SiteInfo, SiteTag


# Create your views here.

def index(request):
	sites = SiteInfo.objects.order_by('-date')
	tags = SiteTag.objects.all()
	return render(request, 'index.html', {'tags': tags, 'sites': sites})


def tag_info(request, st):
	tag = get_object_or_404(SiteTag, tag_name=st)
	return render(request, 'tag_info.html', {'tag': tag})


def site_info(request, st):
	site = get_object_or_404(SiteInfo, title=st)
	site_content = []
	return render(request, 'site.html', {'site': site, 'site_content': site_content})

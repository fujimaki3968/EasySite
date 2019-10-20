# Generated by Django 2.2.6 on 2019-10-20 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_mediaimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinfo',
            name='thumbnail',
            field=models.ManyToManyField(blank=True, to='website.MediaImage'),
        ),
        migrations.AlterField(
            model_name='mediaimage',
            name='attach',
            field=models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='添付ファイル'),
        ),
    ]
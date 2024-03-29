# Generated by Django 2.2.2 on 2019-10-18 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20191018_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitetag',
            name='tag_name',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='visitlog',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.SiteInfo'),
        ),
    ]

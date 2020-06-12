# Generated by Django 3.0.3 on 2020-05-21 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_auto_20200518_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='app_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='subtitle',
            field=models.CharField(default='Project subtitle', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='summary',
            field=models.TextField(default='summary summary summary', max_length=250),
            preserve_default=False,
        ),
    ]
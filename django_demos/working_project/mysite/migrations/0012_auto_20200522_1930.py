# Generated by Django 3.0.3 on 2020-05-23 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_categorytag_display_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytag',
            name='display_title',
            field=models.CharField(max_length=25),
        ),
    ]

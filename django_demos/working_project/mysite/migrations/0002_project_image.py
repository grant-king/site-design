# Generated by Django 3.0.3 on 2020-05-19 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='project_pics'),
        ),
    ]

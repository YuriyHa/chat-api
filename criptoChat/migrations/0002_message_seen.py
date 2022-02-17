# Generated by Django 4.0 on 2022-02-16 15:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('criptoChat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='seen',
            field=models.ManyToManyField(related_name='seen', to=settings.AUTH_USER_MODEL),
        ),
    ]

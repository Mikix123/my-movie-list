# Generated by Django 2.2.7 on 2019-11-12 12:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='createAt',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-26 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_alter_event_rrule'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='exDate',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-19 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_event_todoid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='todoID',
            new_name='associatedTodo',
        ),
    ]
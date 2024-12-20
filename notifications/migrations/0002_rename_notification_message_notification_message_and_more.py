# Generated by Django 5.1.2 on 2024-11-11 08:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='notification_message',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='notification_title',
            new_name='title',
        ),
        migrations.AddField(
            model_name='notification',
            name='date_sent',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 4.1.7 on 2023-06-06 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0004_articleblock'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='puplished',
            field=models.BooleanField(default=False),
        ),
    ]

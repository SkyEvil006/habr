# Generated by Django 4.2.2 on 2023-06-15 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0011_like'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'permissions': [('can_read_article', 'can read article')]},
        ),
    ]

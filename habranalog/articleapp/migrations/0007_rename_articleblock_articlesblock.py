# Generated by Django 4.1.7 on 2023-06-07 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0006_rename_puplished_article_published'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ArticleBlock',
            new_name='ArticlesBlock',
        ),
    ]
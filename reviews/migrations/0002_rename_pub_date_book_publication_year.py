# Generated by Django 4.0.5 on 2022-08-24 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='pub_date',
            new_name='publication_year',
        ),
    ]
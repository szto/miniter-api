# Generated by Django 2.2 on 2019-04-24 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='pub_data',
            new_name='pub_date',
        ),
    ]

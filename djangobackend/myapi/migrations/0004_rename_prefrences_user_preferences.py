# Generated by Django 4.2.2 on 2023-06-18 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_alter_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='prefrences',
            new_name='preferences',
        ),
    ]
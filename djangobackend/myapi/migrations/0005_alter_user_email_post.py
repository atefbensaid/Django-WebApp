# Generated by Django 4.2.2 on 2023-06-18 19:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_rename_prefrences_user_preferences'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('salary_min', models.IntegerField(default=0)),
                ('salary_max', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='myapi.user')),
            ],
        ),
    ]

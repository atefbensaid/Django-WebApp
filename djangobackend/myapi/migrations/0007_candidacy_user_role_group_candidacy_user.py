# Generated by Django 4.2.2 on 2023-06-18 20:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0006_user_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidacy',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('salary_min', models.IntegerField(default=0)),
                ('salary_max', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default=1, max_length=20),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('candidacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='myapi.candidacy')),
            ],
        ),
        migrations.AddField(
            model_name='candidacy',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidacies', to='myapi.user'),
        ),
    ]

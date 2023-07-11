import uuid
from django.db import models
from django.utils import timezone


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, default=0)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(default=timezone.now)
    activated = models.BooleanField(default=False)
    preferences = models.JSONField()

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary_min = models.IntegerField(default=0)
    salary_max = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Candidacy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, default=0)
    location = models.CharField(max_length=100)
    salary_exp = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    candidate = models.ForeignKey('Candidate', on_delete=models.CASCADE, default=1)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, default=0)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(default=timezone.now)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    candidacy = models.ForeignKey('Candidacy', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
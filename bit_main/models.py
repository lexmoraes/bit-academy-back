import uuid
from django.core.validators import MinLengthValidator
from django.db import models


class ModelBase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class User(ModelBase):
    id_user = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    username = models.CharField(
        MinLengthValidator(6),
        max_length=12,
        unique=True
    )
    name = models.CharField(max_length=30)
    email = models.EmailField(
        max_length=150,
        unique=True,
    )
    password = models.TextField(MinLengthValidator(8))
    xp = models.IntegerField(default=0)
    streak = models.IntegerField(default=0)

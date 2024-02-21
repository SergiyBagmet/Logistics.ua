from enum import Enum

from django.db import models
from django.contrib.auth.models import User


class Role(Enum):
    ADMIN = "admin"
    USER = "user"
    EXECUTOR = "executor"
    CUSTOMER = "customer"

    @classmethod
    def choices(cls):
        return [(role.value, role.name) for role in cls]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=Role.choices(), default=Role.USER.value)
    phone = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

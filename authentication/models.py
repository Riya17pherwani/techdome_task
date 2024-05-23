from django.db import models
from django.contrib.auth.models import AbstractUser
from enum import IntEnum


class ROLES(IntEnum):
    USER = 1
    ADMIN = 2


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    roles = models.IntegerField(
        choices=[(tag.value, tag.name) for tag in ROLES],
        default=ROLES.USER.value
    )
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser'
    )

    def __str__(self):
        return self.email

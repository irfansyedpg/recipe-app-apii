
"""
Database Models
"""

from typing import Any
from django.db import models

from django.contrib.auth.models import(
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    """ Manager for User model"""

    def create_user(self,email,password=None,**extra_field):
        user = self.model(email=email,**extra_field)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser,PermissionsMixin):
    """ User in the System."""
    email = models.EmailField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager

    USERNAME_FIELD = 'email'
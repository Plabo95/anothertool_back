from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        "Creates and saves a new user"

        if not email:
            raise ValueError('Es obligatorio introducir un email')

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None, **kwargs):
        "Creates and saves a new superuser"

        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):

    "CUstom user model without username, only email"
    email = models.EmailField(max_length=255 ,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
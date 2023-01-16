from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        "Creates and saves a new user"
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):

    "CUstom user model without username, only email"
    email = models.EmailField(max_length=255 ,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
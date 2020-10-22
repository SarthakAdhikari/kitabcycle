from django.contrib.gis.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db.models.signals import post_save
from django.conf import settings


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            # otherwise it returns TypeError if we pass email=None
            raise ValueError("Users must have an email address.")
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'


    # get_user_model().objects.create(username=email, password=password)
class Profile(models.Model):
    name = models.CharField(max_length=250)
    bio = models.CharField(max_length=1000)
    location_point = models.PointField(blank=True, null=True, srid=4326)
    phone_number = models.BigIntegerField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """manager for user Profiles"""
    def create_user(self,email,name,password=None):
        """Create a new User profie"""
        if not email:
            raise ValueError("users must have an Email address")
        email= self.normalize_email(email)
        user= self.model(email=email,name=name)

        user.self_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        """create and save a new Super user with given details"""
        user=self.create_user(email,name,password)

        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the System"""
    email= models.EmailField(max_length=225,unique=True)
    name = models.CharField(max_length=225)
    is_active = models.BooleanField(default=True)
    is_staff =models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["name"]

    def get_full_name(self):
        """Retrive full name of user"""
        return self.name
    def get_short_name(self):
        """retrive small name of the users"""
        return self.name

    def __str__(self):
        """return string respertation of our user"""
        return self.email

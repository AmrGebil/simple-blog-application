from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# This class toManage user creation with required fields and superuser creation with additional privileges.

class MyAccountManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not email:
            raise  ValueError('user must have email address')
        if not username:
            raise  ValueError('user must have username')
        user =self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,username,email,password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,

        )
        user.is_admin=True
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True

        user.save(using=self._db)
        return user


# This class to Defintion a custom user model with specified fields and permissions, extending AbstractBaseUser and using MyAccountManager for user management.

class Account(AbstractBaseUser):
    username= models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=100,unique=True)

    #required
    data_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects=MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,add_label):
        return True





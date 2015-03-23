# coding=utf-8
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, username, telephone, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            telephone=telephone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username, password, telephone=""):
        """
        Creates and saves a superuser with the given email, username and password.
        """
        user = self.create_user(email=email,
                                username=username,
                                password=password,
                                telephone=telephone
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    #注意：不继承PermissionsMixin类，是无法实现使用Django Group功能的，本人的项目需要使用所以继承该类。
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    # 用户登录名
    username = models.CharField(max_length=100, unique=True, db_index=True)
    # 英文名
    first_name = models.CharField(max_length=100, unique=True, db_index=True)
    # 英文姓
    last_name = models.CharField(max_length=100, unique=True, db_index=True)
    # 中文姓名
    cn_name = models.CharField(max_length=100, unique=True, db_index=True)

    avatar = models.URLField(blank=True)

    telephone = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()
    # !!!
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Calender(models.Model):
    """日历"""
    year = models.SmallIntegerField('年')
    month = models.SmallIntegerField('月')
    day = models.SmallIntegerField('日')
    # 1=是节假日
    is_holiday = models.SmallIntegerField('是节假日', default=0)
    holiday_mark = models.CharField('节假日说明', max_length=50)


# coding=utf-8
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


# todo: Group设置：供应商组，采购商组？
class Org(models.Model):
    """组织"""
    name = models.CharField('名称', max_length=50)
    code = models.CharField('编码', max_length=50)
    location = models.CharField('位置', max_length=200, null=True)
    telephone = models.CharField('手机', max_length=30, null=True)
    phone = models.CharField('固话', max_length=30, null=True)
    url = models.URLField('链接地址', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


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
    org = models.ForeignKey(Org, null=True)
    #注意：不继承PermissionsMixin类，是无法实现使用Django Group功能的，本人的项目需要使用所以继承该类。
    email = models.EmailField(verbose_name='email address', max_length=255, null=True, unique=True)
    # 用户登录名
    username = models.CharField(max_length=100, unique=True, db_index=True)
    # 英文名
    first_name = models.CharField(max_length=100, db_index=True)
    # 英文姓
    last_name = models.CharField(max_length=100, null=True, db_index=True)
    # 中文姓名
    cn_name = models.CharField(max_length=100, unique=True, null=True, db_index=True)

    avatar = models.URLField(blank=True)

    telephone = models.CharField(null=True, max_length=50)

    created_at = models.DateTimeField(null=True, auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    qq = models.CharField(null=True, max_length=20)
    idcard_no = models.CharField(null=True, max_length=50)
    hired_at = models.DateTimeField(null=True, auto_now_add=True)

    birthday = models.DateField(null=True)
    gender = models.IntegerField(null=True, default=1)
    # 离职
    quited = models.IntegerField(null=True, default=0)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.username

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


class Calendar(models.Model):
    """日历"""
    year = models.SmallIntegerField('年')
    month = models.SmallIntegerField('月')
    day = models.SmallIntegerField('日')
    # 1=是节假日
    is_holiday = models.BooleanField('是节假日', default=False)
    holiday_mark = models.CharField('节假日说明', null=True, max_length=50)

    def get_full_datetime(self):
        # todo: 返回datetime()格式
        return '%s-%s-%s' % (self.year, self.month, self.day)

    def __unicode__(self):
        return self.get_full_datetime()


class Conf(models.Model):
    """配置"""
    name = models.CharField('名称', max_length=50)
    content = models.CharField('内容', max_length=100)
    desc = models.CharField('配置说明', max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name





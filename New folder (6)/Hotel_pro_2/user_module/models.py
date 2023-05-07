from django.db import models


# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=50, verbose_name='نام')
    password = models.CharField(max_length=100, verbose_name='رمز')
    email = models.CharField(max_length=500, verbose_name='ایمیل')
    profile_pic = models.ImageField(upload_to='uploads', null=False, blank=True, verbose_name='پروفایل')
    phone_number = models.CharField(max_length=50, verbose_name='تلفن همراه')
    gender = models.CharField(max_length=50, null=False, blank=False, verbose_name='جنسیت')

    def __str__(self):
        return f'manager room : {self.user_name}'

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


class Customer(models.Model):
    user_name = models.CharField(max_length=300, verbose_name='نام')
    password = models.CharField(max_length=300, verbose_name='رمز')
    email = models.CharField(max_length=500, verbose_name='ایمیل')
    profile_pic = models.ImageField(upload_to='uploads', null=False, blank=True, verbose_name='پروفایل')
    phone_number = models.CharField(max_length=50, verbose_name='تلفن همراه')
    address = models.CharField(max_length=500, verbose_name='ادرس')
    pin_code = models.IntegerField(blank=True)

    def __str__(self):
        return f'Customer : {self.user_name}'

    class Meta:
        verbose_name = 'تنظیمات کاربر'
        verbose_name_plural = 'تنظیمات کاربران'


class Admin(models.Model):
    name = models.CharField(max_length=300, verbose_name='نام')
    email = models.CharField(max_length=500, verbose_name='ایمیل')
    phone = models.CharField(max_length=300, verbose_name='تلفن همراه')
    gender = models.CharField(max_length=300, null=False, blank=False, verbose_name='جنسیت')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ادمین'
        verbose_name_plural = 'ادمین ها'

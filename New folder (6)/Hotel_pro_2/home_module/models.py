from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from user_module.models import User, Customer, Admin


# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=500, verbose_name='نام')
    email = models.EmailField(max_length=500, verbose_name='ایمیل')
    massage = models.CharField(max_length=1000, verbose_name='متن')
    massage_admin = models.CharField(max_length=1000, verbose_name='متن ادمین', null=True, blank=True)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE, null=True, blank=True, verbose_name='توسط ادمین')
    see_text = models.BooleanField(default=False, verbose_name='دیده شده / نشده')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(args, kwargs)
    #     self.subject = None

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'


class SettingSite_header(models.Model):
    title = models.CharField(max_length=3000, verbose_name='نام')
    description = models.CharField(max_length=1000, verbose_name='توضیحات')
    address = models.CharField(max_length=10000, verbose_name='آدرس')
    title_room = models.CharField(max_length=500, verbose_name='نام اتاق')
    description_room = models.CharField(max_length=1000, verbose_name='توضیحات اتاق')
    is_main_setting = models.BooleanField(default=True, verbose_name='تنظیمات اصلی')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تنظیم بالای سایت'
        verbose_name_plural = 'تنظیمات بالای سایت'


class FoodsHotel(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام')
    description = models.CharField(max_length=1000, verbose_name='توضیحات')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تنظیمات غذا'
        verbose_name_plural = 'تنظیمات غذا ها'


class Rooms(models.Model):
    rooms = models.CharField(max_length=60, verbose_name='تعداد اتاق')
    room_type = models.CharField(max_length=60, verbose_name='نوع اتاق')
    price = models.CharField(max_length=5000, verbose_name='قیمت')
    manager = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True, verbose_name='کاربران')
    score = models.IntegerField(verbose_name='شناسه')
    start_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='تاریخ ورود')
    room_image = models.ImageField(upload_to='uploads', null=False, blank=False, verbose_name='عکس اتاق ها')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    def __str__(self):
        return f'Room now : {self.id}'

    class Meta:
        verbose_name = 'اتاق'
        verbose_name_plural = 'اتاق ها'


class Booking(models.Model):
    # room_number = models.ForeignKey(Rooms, on_delete=models.CASCADE, verbose_name='تعداد اتاق ها')
    room_number = models.IntegerField(verbose_name='تعداد اتاق ها')
    # user_id = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='ای دی کاربران')
    start_date = models.DateField(verbose_name='تاریخ ورود')
    end_date = models.DateField(verbose_name='تاریخ خروج')
    booked_on = models.DateField(auto_now_add=True, verbose_name='رزرو')

    def __str__(self):
        return f'Booking ID : {str(self.id)}'

    class Meta:
        verbose_name = 'رزرو'
        verbose_name_plural = 'لیست رزرو ها'

    @property
    def is_past_due(self):
        return date.today() > self.end_date


class AboutSite(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام')
    description = models.CharField(max_length=1000, verbose_name='توضیحات')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'


class Moshtari(models.Model):
    title = models.CharField(max_length=500, verbose_name='نام')
    description = models.CharField(max_length=1000, verbose_name='توضیحات')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتری ها'


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100, verbose_name='نام وبسایت')
    site_url = models.CharField(max_length=100, verbose_name='دامنه وبسایت')
    address = models.CharField(max_length=100, verbose_name='آدرس')
    phone = models.CharField(max_length=100, null=True, blank=True, verbose_name='تلفن ')
    fax = models.CharField(max_length=100, null=True, blank=True, verbose_name='فکس ')
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name='ایمیل ')
    copy_right = models.TextField(verbose_name='متن کپی رایت وبسایت')
    about_us_text = models.TextField(verbose_name='متن درباره ما سایت')
    site_logo = models.ImageField(verbose_name='لوگو سایت', upload_to='uploads/site_setting')
    is_main_setting = models.BooleanField(verbose_name='تنظیمات اصلی')

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'


class ContactUsModel(models.Model):
    name = models.CharField(max_length=500, verbose_name='نام')
    email = models.EmailField(max_length=500, verbose_name='ایمیل')
    massage = models.CharField(max_length=1000, verbose_name='متن')
    massage_admin = models.CharField(max_length=1000, verbose_name='متن ادمین')
    see_text = models.BooleanField(default=False, verbose_name='دیده شده / نشده')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'ارتباط با ما'
        verbose_name_plural = 'ارتباتاط با ما'


class Room(models.Model):
    name = models.CharField(max_length=200, verbose_name='اسم اتاق')
    description = models.TextField(verbose_name='توضیحات')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='قیمت')

    def str(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hotel:room_detail', args=[str(self.id)])


class Reservation(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    phone_number = models.CharField(max_length=20, verbose_name='تلفن همراه')
    check_in_date = models.DateField(verbose_name='تاریخ ورود')
    check_out_date = models.DateField(verbose_name='تاریخ خروج')
    number_of_guests = models.IntegerField(verbose_name='تعداد مهمان ها')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='اتاق')

    def str(self):
        return self.name

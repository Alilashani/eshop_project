from django.db import models


# Create your models here.


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100, verbose_name='نام وبسایت')
    site_url = models.CharField(max_length=100, verbose_name='دامنه وبسایت')
    address = models.CharField(max_length=100, verbose_name='آدرس')
    phone = models.CharField(max_length=100, null=True, blank=True, verbose_name='تلفن ')
    fax = models.CharField(max_length=100, null=True, blank=True, verbose_name='فکس ')
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name='ایمیل ')
    copy_right = models.TextField(verbose_name='متن کپی رایت وبسایت')
    about_us_text = models.TextField(verbose_name='متن درباره ما سایت')
    site_logo = models.ImageField(verbose_name='لوگو سایت', upload_to='images/site_setting')
    is_main_setting = models.BooleanField(verbose_name='تنظیمات اصلی')

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')

    class Meta:
        verbose_name = 'دسته بندی لینک های فوتر'
        verbose_name_plural = 'دسته بندی های لینک های فوتر'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')
    footer_link_box = models.ForeignKey(to=FooterLinkBox, verbose_name='دسته بندی', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینک های فوتر'

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')
    url_title = models.CharField(max_length=200, verbose_name='عنوان لینک')
    description = models.TextField(verbose_name='توضیحات اسلایدر')
    image = models.ImageField(upload_to='images/sliders', verbose_name='تصویر اسلایدر')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return self.title


class SiteBanner(models.Model):
    class SiteBannerPositions(models.TextChoices):
        product_list = 'product_list', 'صفحه لیست محصولات',
        product_ditail = 'product_ditail', 'صفحه جزیات محصولات'
        about_us = 'about_us', 'صفحه درباره ما'

    title = models.CharField(max_length=300, verbose_name='عنوان')
    url = models.URLField(max_length=400, null=True, blank=True, verbose_name='آدرس لینک')
    image = models.ImageField(upload_to='images/banners', verbose_name='تصویر')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    position = models.CharField(max_length=200, choices=SiteBannerPositions.choices, verbose_name='محل قرار گیری')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'بنر تبلیغاتی'
        verbose_name_plural = 'بنر های تبلیغاتی'

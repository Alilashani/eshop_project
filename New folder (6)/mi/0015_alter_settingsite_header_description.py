# Generated by Django 4.1.5 on 2023-03-04 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0014_settingsite_header_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingsite_header',
            name='description',
            field=models.CharField(max_length=1000, verbose_name='توضیحات'),
        ),
    ]
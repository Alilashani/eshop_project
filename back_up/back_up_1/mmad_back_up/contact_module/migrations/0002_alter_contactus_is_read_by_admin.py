# Generated by Django 3.2.7 on 2022-01-06 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='is_read_by_admin',
            field=models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین'),
        ),
    ]
# Generated by Django 4.1 on 2022-12-02 14:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0006_article_crate_date_alter_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='crate_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2022, 12, 2), verbose_name='تاریخ ثبت'),
            preserve_default=False,
        ),
    ]

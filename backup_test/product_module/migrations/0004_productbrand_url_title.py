# Generated by Django 4.1 on 2022-12-13 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0003_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productbrand',
            name='url_title',
            field=models.CharField(db_index=True, default='url_title', max_length=300, verbose_name='نام لینک'),
            preserve_default=False,
        ),
    ]

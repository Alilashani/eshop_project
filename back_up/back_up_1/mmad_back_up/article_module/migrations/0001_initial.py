# Generated by Django 4.1 on 2022-12-01 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('url_title', models.CharField(max_length=200, verbose_name='عنوان لینک')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیر فعال')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقاله ها',
            },
        ),
    ]

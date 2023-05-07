# Generated by Django 4.1 on 2022-12-04 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article_module', '0007_alter_article_crate_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('text', models.TextField(verbose_name='متن نظر')),
                ('is_ok', models.BooleanField(default=False, verbose_name='فعال / غیرفعال')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article_module.article', verbose_name='مقاله')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article_module.articlecomment', verbose_name='والد')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
        ),
    ]

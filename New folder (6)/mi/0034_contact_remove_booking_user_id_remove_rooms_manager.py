# Generated by Django 4.1.5 on 2023-03-11 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0033_contactusmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='نام')),
                ('email', models.EmailField(max_length=500, verbose_name='ایمیل')),
                ('see_text', models.BooleanField(default=False, verbose_name='دیده شده / نشده')),
            ],
            options={
                'verbose_name': 'تماس با ما',
                'verbose_name_plural': 'لیست تماس با ما',
            },
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='manager',
        ),
    ]
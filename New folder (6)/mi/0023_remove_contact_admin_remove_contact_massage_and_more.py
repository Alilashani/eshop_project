# Generated by Django 4.1.5 on 2023-03-08 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0022_contact_subject_alter_moshtari_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='massage',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='massage_admin',
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=10000, verbose_name='subject'),
        ),
    ]

# Generated by Django 4.1 on 2022-12-04 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0008_articlecomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlecomment',
            options={'verbose_name': 'نظر مقاله', 'verbose_name_plural': 'نظرات مقاله ها'},
        ),
        migrations.RenameField(
            model_name='articlecomment',
            old_name='create_date',
            new_name='create_data',
        ),
        migrations.RenameField(
            model_name='articlecomment',
            old_name='is_ok',
            new_name='is_active',
        ),
    ]
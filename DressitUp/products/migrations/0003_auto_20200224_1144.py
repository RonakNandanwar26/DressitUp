# Generated by Django 2.2.10 on 2020-02-24 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200224_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='image2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='image3'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='image4'),
        ),
    ]

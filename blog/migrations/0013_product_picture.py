# Generated by Django 3.2.13 on 2023-03-12 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_product_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, upload_to='media', verbose_name='Изображение'),
        ),
    ]
# Generated by Django 3.2.13 on 2023-03-15 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(null=True, upload_to='', verbose_name='Изображение'),
        ),
    ]
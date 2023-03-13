# Generated by Django 3.2.13 on 2023-03-12 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20220912_0123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={},
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('(готовый товар)', 'готовый товар'), ('(на заказ)', 'на заказ')], max_length=20, verbose_name='Статус товара'),
        ),
    ]

# Generated by Django 3.2.18 on 2023-03-30 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='adress',
        ),
    ]
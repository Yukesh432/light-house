# Generated by Django 3.1.1 on 2020-10-05 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20201005_0054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='price',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='product',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='quantity',
        ),
    ]

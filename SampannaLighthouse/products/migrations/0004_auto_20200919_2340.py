# Generated by Django 3.1.1 on 2020-09-19 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200919_2306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='phone_number',
            new_name='phone',
        ),
    ]
# Generated by Django 5.1.3 on 2024-12-13 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coder_app', '0010_order_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='features',
        ),
    ]
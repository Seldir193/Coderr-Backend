# Generated by Django 5.1.3 on 2024-12-16 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder_app', '0014_order_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessprofile',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='businessprofile',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
    ]
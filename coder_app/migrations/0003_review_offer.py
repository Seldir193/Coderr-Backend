# Generated by Django 5.1.3 on 2024-12-09 20:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder_app', '0002_order_business_user_alter_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='offer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offer_reviews', to='coder_app.offer'),
        ),
    ]

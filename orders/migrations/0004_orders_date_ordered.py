# Generated by Django 3.0.2 on 2020-07-19 19:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_map'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='date_ordered',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
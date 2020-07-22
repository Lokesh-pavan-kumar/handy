# Generated by Django 3.0.4 on 2020-07-20 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_orders_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_status',
            field=models.CharField(choices=[('Pr', 'Processing'), ('Re', 'Recieved'), ('Wa', 'Waiting'), ('Sh', 'Shipped'), ('De', 'Delivered')], default='Delivered', max_length=10),
        ),
    ]
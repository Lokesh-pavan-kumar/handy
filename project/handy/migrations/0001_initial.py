# Generated by Django 3.0.2 on 2020-02-23 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True
    atomic = False

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artisans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=30)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='thumbnail_pics')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('availability', models.BooleanField(default=False)),
                ('artisan_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='handy.Artisans')),
            ],
        ),
    ]
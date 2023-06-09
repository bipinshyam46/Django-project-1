# Generated by Django 4.1.7 on 2023-04-04 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('token', models.IntegerField(verbose_name='Token')),
                ('order_date', models.DateField(auto_now_add=True)),
                ('order_id', models.CharField(max_length=200, verbose_name='Order id')),
                ('payment_mode', models.CharField(max_length=200, verbose_name='Payment mode')),
                ('payment_id', models.CharField(max_length=200, verbose_name='Payment id')),
                ('status', models.CharField(choices=[('pending', 'pending'), ('accepted', 'accepted'), ('out for delivery', 'out for delivery'), ('completed', 'completed')], default='pending', max_length=150, verbose_name='Order status')),
                ('total_price', models.FloatField(verbose_name='Total price')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.items')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 3.1.12 on 2025-01-20 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_product_stockmovement'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sale_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.product')),
            ],
        ),
    ]

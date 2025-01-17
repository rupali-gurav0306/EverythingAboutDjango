# Generated by Django 5.0.3 on 2024-04-17 06:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('payment_mode', models.CharField(choices=[('Cash', 'Cash'), ('Debit Card', 'Debit Card'), ('Credit Card', 'Credit Card'), ('PayTM', 'PayTM'), ('Online Pay', 'Online Pay')], max_length=100)),
                ('payment_date', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SMS.student')),
            ],
        ),
    ]

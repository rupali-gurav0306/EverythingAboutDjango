# Generated by Django 5.0.4 on 2024-04-29 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0003_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdetails',
            name='payment_mode',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Debit Card', 'Debit Card'), ('CreditCard', 'Credit Card'), ('PayTM', 'PayTM'), ('Online Pay', 'Online Pay')], max_length=100),
        ),
    ]

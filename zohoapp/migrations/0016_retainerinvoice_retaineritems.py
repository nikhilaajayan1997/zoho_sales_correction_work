# Generated by Django 4.1.7 on 2023-09-06 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0015_remove_retaineritems_retainer_delete_retainerinvoice_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RetainerInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('retainer_invoice_number', models.CharField(max_length=255)),
                ('refrences', models.CharField(max_length=255)),
                ('retainer_invoice_date', models.DateField()),
                ('total_amount', models.CharField(max_length=100)),
                ('customer_notes', models.TextField()),
                ('terms_and_conditions', models.TextField()),
                ('is_draft', models.BooleanField(default=True)),
                ('is_sent', models.BooleanField(default=False)),
                ('customer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.customer')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Retaineritems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('amount', models.CharField(max_length=100)),
                ('retainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.retainerinvoice')),
            ],
        ),
    ]

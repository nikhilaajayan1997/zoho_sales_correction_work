# Generated by Django 4.1.7 on 2023-08-24 07:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0011_remove_invoice_item_inv_delete_invoice_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.TextField(max_length=255)),
                ('terms', models.CharField(max_length=100)),
                ('order_no', models.IntegerField()),
                ('inv_date', models.DateField()),
                ('due_date', models.DateField()),
                ('igst', models.TextField(max_length=255)),
                ('cgst', models.TextField(max_length=255)),
                ('sgst', models.TextField(max_length=255)),
                ('t_tax', models.FloatField()),
                ('subtotal', models.FloatField()),
                ('grandtotal', models.FloatField()),
                ('cxnote', models.TextField(max_length=255)),
                ('file', models.ImageField(upload_to='documents')),
                ('terms_condition', models.TextField(max_length=255)),
                ('status', models.TextField(max_length=255)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.customer')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
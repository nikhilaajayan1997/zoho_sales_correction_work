# Generated by Django 4.1.7 on 2023-09-18 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0022_invoice_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice_comments',
            name='invoice',
        ),
        migrations.RemoveField(
            model_name='invoice_comments',
            name='user',
        ),
        migrations.RemoveField(
            model_name='invoice_item',
            name='inv',
        ),
        migrations.DeleteModel(
            name='invoice',
        ),
        migrations.DeleteModel(
            name='invoice_comments',
        ),
        migrations.DeleteModel(
            name='invoice_item',
        ),
    ]

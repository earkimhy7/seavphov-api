# Generated by Django 2.2.1 on 2019-05-28 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Type',
            new_name='SellerType',
        ),
        migrations.RenameField(
            model_name='seller',
            old_name='type',
            new_name='seller_type',
        ),
    ]

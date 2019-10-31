# Generated by Django 2.2.1 on 2019-06-10 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventories', '0003_condition_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventories', to='inventories.Detail'),
        ),
    ]
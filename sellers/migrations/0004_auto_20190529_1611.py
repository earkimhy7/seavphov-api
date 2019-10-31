# Generated by Django 2.1.5 on 2019-05-29 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0003_auto_20190529_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='address',
        ),
        migrations.AddField(
            model_name='seller',
            name='communes',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='countries',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='district',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='house_number',
            field=models.TextField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='postal_code',
            field=models.TextField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='province_city',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='street_number',
            field=models.TextField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='village',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
    ]
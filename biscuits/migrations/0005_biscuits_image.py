# Generated by Django 5.1.6 on 2025-03-05 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biscuits', '0004_remove_biscuits_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='biscuits',
            name='image',
            field=models.CharField(default='abc', max_length=1000),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.1.6 on 2025-02-27 15:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biscuits', '0001_initial'),
        ('pairings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='biscuits',
            name='pairing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matched_biscuit', to='pairings.pairings'),
        ),
    ]

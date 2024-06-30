# Generated by Django 5.0.6 on 2024-06-30 00:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propiedades', '0004_alter_comuna_region_alter_propiedad_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='propiedades.region', verbose_name='Región'),
        ),
    ]

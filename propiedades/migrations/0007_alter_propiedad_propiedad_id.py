# Generated by Django 5.0.6 on 2024-06-30 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propiedades', '0006_propiedad_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='propiedad_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

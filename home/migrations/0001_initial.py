# Generated by Django 5.0.2 on 2024-11-10 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=100)),
                ('item_price', models.IntegerField()),
                ('item_description', models.TextField()),
                ('barcode', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]

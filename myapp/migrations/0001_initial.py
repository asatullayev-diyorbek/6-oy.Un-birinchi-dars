# Generated by Django 5.1.1 on 2024-09-05 07:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Brend',
                'verbose_name_plural': 'Brendlar',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_manufactured', models.DateField()),
                ('count', models.IntegerField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.brand')),
            ],
            options={
                'verbose_name': 'Avtomobil',
                'verbose_name_plural': 'Avtomobillar',
            },
        ),
    ]

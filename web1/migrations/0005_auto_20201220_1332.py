# Generated by Django 3.1.4 on 2020-12-20 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web1', '0004_auto_20201220_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
# Generated by Django 3.1.4 on 2021-01-14 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web1', '0008_auto_20210106_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]

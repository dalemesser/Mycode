# Generated by Django 3.1.4 on 2021-01-22 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web1', '0011_customer_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]